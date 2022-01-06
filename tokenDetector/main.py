# Given 10 JavaScript files, write a regular expression script to search the code in all of these files for any
# private keys or things that look like tokens. The result should return the following: - The name of the file(s) -
# The line numbers of where the private keys or tokens start and end.
# ----------------------------------------------------------------------------------------------------------------------


from typing import List, Tuple
import re
# ----------------------------------------------------------------------------------------------------------------------


class TokenFinder:
    def __init__(self):
        self.pattern = r'(?:[A-Za-z0-9+/]{4})+(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?'

    def find_start_lines(self, folder_path: str) -> List[Tuple[str, int, int]]:
        test = '''
aws_access_key_id="KIAIOSFODNN7EXAMPLE";
aws_access_key_id=" KIAIOSFODNN7EXAMPLE  ";
aws_secret_access_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY";
aws_access_key=dasdasd;
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAACmFlczI1Ni1jdHIAAAAGYmNyeXB0AAAAGAAAABBF/wJY9k
b3BlbnNzaC1rZXktdjEAAAAACmFlczI1Ni1jdHIAAAAGYmNyeXB0AAAAGAAAABBF/wJY9k
Wz1wz3F503/VL0zY1J481IWbKsmaVWbp/7HOos2wuoRj0u
-----END OPENSSH PRIVATE KEY-----
        '''

        result = re.findall(self.pattern, test)

        peaks = []

        return peaks


# ----------------------------------------------------------------------------------------------------------------------


token_finder = TokenFinder()
for filename, start_line, end_line in token_finder.find_start_lines('./js_files'):
    print("%s - %d - %d" % (filename, start_line, end_line))
# ----------------------------------------------------------------------------------------------------------------------
