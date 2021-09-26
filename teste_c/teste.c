#include <stdint.h>
#include <math.h>
#include <stdio.h>

float sqrt_lut(const float* lut, int lutLen, float num)
{
    float result = -1;
    if(num >= 0)
    {
        int pos = (int)num;
        if(pos < lutLen)
            result = lut[pos];
    }
    return result;    
}

int main()
{
    const float lut[256] = {
        0.000000f, 1.000000f, 1.414214f, 1.732051f, 2.000000f, 2.236068f, 2.449490f, 2.645751f, 2.828427f, 3.000000f, 3.162278f, 3.316625f, 3.464102f, 3.605551f, 3.741657f, 3.872983f, 4.000000f, 
        4.123106f, 4.242640f, 4.358899f, 4.472136f, 4.582576f, 4.690416f, 4.795832f, 4.898980f, 5.000000f, 5.099020f, 5.196152f, 5.291502f, 5.385165f, 5.477226f, 5.567764f, 5.656854f, 
        5.744563f, 5.830952f, 5.916080f, 6.000000f, 6.082763f, 6.164414f, 6.244998f, 6.324555f, 6.403124f, 6.480741f, 6.557438f, 6.633250f, 6.708204f, 6.782330f, 6.855655f, 6.928203f, 
        7.000000f, 7.071068f, 7.141428f, 7.211102f, 7.280110f, 7.348469f, 7.416198f, 7.483315f, 7.549834f, 7.615773f, 7.681146f, 7.745967f, 7.810250f, 7.874008f, 7.937254f, 8.000000f, 
        8.062258f, 8.124039f, 8.185352f, 8.246211f, 8.306623f, 8.366600f, 8.426149f, 8.485281f, 8.544003f, 8.602325f, 8.660254f, 8.717798f, 8.774964f, 8.831760f, 8.888194f, 8.944272f, 
        9.000000f, 9.055386f, 9.110434f, 9.165152f, 9.219544f, 9.273619f, 9.327379f, 9.380832f, 9.433981f, 9.486833f, 9.539392f, 9.591663f, 9.643651f, 9.695360f, 9.746795f, 9.797959f, 
        9.848858f, 9.899495f, 9.949874f, 10.000000f, 10.049875f, 10.099504f, 10.148891f, 10.198039f, 10.246951f, 10.295630f, 10.344080f, 10.392304f, 10.440307f, 10.488089f, 10.535654f, 10.583005f, 
        10.630146f, 10.677078f, 10.723805f, 10.770329f, 10.816654f, 10.862781f, 10.908712f, 10.954452f, 11.000000f, 11.045361f, 11.090536f, 11.135529f, 11.180340f, 11.224972f, 11.269427f, 11.313708f, 
        11.357817f, 11.401754f, 11.445523f, 11.489125f, 11.532562f, 11.575837f, 11.618950f, 11.661903f, 11.704700f, 11.747340f, 11.789826f, 11.832160f, 11.874342f, 11.916375f, 11.958261f, 12.000000f, 
        12.041595f, 12.083046f, 12.124355f, 12.165525f, 12.206555f, 12.247449f, 12.288206f, 12.328828f, 12.369317f, 12.409674f, 12.449900f, 12.489996f, 12.529964f, 12.569805f, 12.609520f, 12.649111f, 
        12.688578f, 12.727922f, 12.767145f, 12.806249f, 12.845233f, 12.884099f, 12.922848f, 12.961481f, 13.000000f, 13.038404f, 13.076696f, 13.114877f, 13.152946f, 13.190906f, 13.228757f, 13.266500f, 
        13.304134f, 13.341664f, 13.379088f, 13.416408f, 13.453624f, 13.490738f, 13.527749f, 13.564660f, 13.601471f, 13.638182f, 13.674794f, 13.711309f, 13.747727f, 13.784049f, 13.820275f, 13.856406f, 
        13.892444f, 13.928389f, 13.964240f, 14.000000f, 14.035668f, 14.071247f, 14.106736f, 14.142136f, 14.177447f, 14.212670f, 14.247807f, 14.282857f, 14.317822f, 14.352700f, 14.387495f, 14.422205f, 
        14.456832f, 14.491377f, 14.525839f, 14.560220f, 14.594520f, 14.628738f, 14.662878f, 14.696939f, 14.730920f, 14.764823f, 14.798649f, 14.832397f, 14.866069f, 14.899665f, 14.933185f, 14.966630f, 
        15.000000f, 15.033297f, 15.066519f, 15.099669f, 15.132746f, 15.165751f, 15.198684f, 15.231546f, 15.264338f, 15.297058f, 15.329710f, 15.362291f, 15.394804f, 15.427249f, 15.459625f, 15.491934f, 
        15.524175f, 15.556349f, 15.588457f, 15.620500f, 15.652476f, 15.684387f, 15.716233f, 15.748015f, 15.779734f, 15.811388f, 15.842979f, 15.874508f, 15.905973f, 15.937377f, 15.968719f, 
    };

    float res[2];
    float res2[2];
    float res3[2];
    float res4[2];

    res[0] = sqrt_lut(lut, 256, 1.5f);
    res[1] = sqrt(1.5f);

    res2[0] = sqrt_lut(lut, 256, 4.5f);
    res2[1] = sqrt(4.5f);

    res3[0] = sqrt_lut(lut, 256, 8.9f);
    res3[1] = sqrt(8.9f);

    res4[0] = sqrt_lut(lut, 256, 9.1f);
    res4[1] = sqrt(9.1f);

    int a = 0;
}