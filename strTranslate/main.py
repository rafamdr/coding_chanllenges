import sys
import re
import translators as ts
# ----------------------------------------------------------------------------------------------------------------------


class SRTTranslator:
    IDX_SEARCH = 1
    TIMESTAMP_SEARCH = 2
    TEXT_SEARCH = 3

    def __init__(self):
        self.dictfunc = {
            self.IDX_SEARCH: self._idx_search,
            self.TIMESTAMP_SEARCH: self._timestamp_search,
            self.TEXT_SEARCH: self._text_search
        }
        self.state = self.IDX_SEARCH
        self.last_state = self.IDX_SEARCH
        self.count_lines = 0

    def _idx_search(self, line):
        if line.strip() != "":
            if re.search(r"[0-9]+\n", line) is None:
                raise Exception("Expecting an idx at line %d" % self.count_lines)
            self.last_state = self.state
            self.state = self.TIMESTAMP_SEARCH
        return line

    def _timestamp_search(self, line):
        # 00:00:47,000 --> 00:00:50,180
        if line.strip() != "":
            if re.search(r"[0-9]+:[0-9]+", line) is None:
                raise Exception("Expecting an timestamp at line %d" % self.count_lines)
            self.last_state = self.state
            self.state = self.TEXT_SEARCH
        return line

    def _text_search(self, line):
        if line.strip() == "":
            res = line + '\n'
            self.last_state = self.state
            self.state = self.IDX_SEARCH
        else:
            res = ts.google(line, to_language='pt', sleep_seconds=0.1, if_use_cn_host=True)
            if line[0].islower():
                res = res[0].lower() + res[1:]
            elif line[0] == ' ':
                if line[1].islower():
                    res = ' ' + res[0].lower() + res[1:]
                else:
                    res = ' ' + res

            if self.last_state == self.TEXT_SEARCH:
                res = '\n' + res
        self.last_state = self.TEXT_SEARCH
        return res

    def translate(self, file_path: str):
        self.state = self.IDX_SEARCH
        self.count_lines = 0
        with open(file_path, 'r') as srt_file:
            with open(file_path + '.txt', 'w') as final_file:
                while line := srt_file.readline():
                    print("Processing line %d..." % self.count_lines)
                    line = self.dictfunc[self.state](line)
                    final_file.write(line)
                    self.count_lines += 1
# ----------------------------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    translator = SRTTranslator()
    translator.translate('/home/rafael/Desktop/test.srt')
# ----------------------------------------------------------------------------------------------------------------------
