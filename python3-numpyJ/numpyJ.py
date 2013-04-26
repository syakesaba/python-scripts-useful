#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Python 3.1.2 (r312:79147, Sep 27 2010, 09:45:41) 
#[GCC 4.4.3] on linux2

#-----------参考
#NumpyのPython3へのインストール
_Install_Numpy_URI=[
"http://home.hiroshima-u.ac.jp/~tyoshida/dokuwiki/python"]
#Numpyのつかいかた
_How2_Numpy_URI=[
"http://d.hatena.ne.jp/pashango_p/20090714/1247590272"
,"http://triplepulu.web.fc2.com/python/numpy.html"
,"http://www.geocities.jp/showa_yojyo/note/python-numpy.html"
,"http://www.logos.ic.i.u-tokyo.ac.jp/~s1s5/pukiwiki/index.php?programming%2Fpython%2Fscipy"
]
try:
    import numpy
except ImportError as e:
    print(e)
    print("See:",_Install_Numpy_URI[0])
Numpy用日本語={
"ALLOW_THREADS":"スレッド対応しているか",
"BUFSIZE":"バッファサイズ",
"CLIP":"クリップ",
"ComplexWarning":"複素数から実数への変換エラー",
"DataSource":"データ存在確認クラス",
"ERR_CALL":"",
"ERR_DEFAULT":"",
"ERR_DEFAULT2":"",
"ERR_IGNORE":"",
"ERR_LOG":"",
"ERR_PRINT":"",
"ERR_RAISE":"",
"ERR_WARN":"",
"FLOATING_POINT_SUPPORT":"",
"FPE_DIVIDEBYZERO":"",
"FPE_INVALID":"",
"FPE_OVERFLOW":"",
"FPE_UNDERFLOW":"",
"False_":"偽",
"Inf":"無限大",
"Infinity":"無限大",
"MAXDIMS":"",
"MachAr":"",
"NAN":"NaN",
"NINF":"負の無限大",
"NZERO":"負のゼロ",
"NaN":"NaN",
"PINF":"正の無限大",
"PZERO":"正のゼロ",
"PackageLoader":"",
"RAISE":"",
"RankWarning":"",
"SHIFT_DIVIDEBYZERO":"",
"SHIFT_INVALID":"",
"SHIFT_OVERFLOW":"",
"SHIFT_UNDERFLOW":"",
"ScalarType":"",
"Tester":"",
"True_":"真",
"UFUNC_BUFSIZE_DEFAULT":"",
"UFUNC_PYVALS_NAME":"",
"WRAP":"",
"abs":"絶対値",
"absolute":"絶対値",
"add":"加算",
"add_docstring":"",
"add_newdoc":"",
"add_newdocs":"",
"alen":"",
"all":"",
"allclose":"",
"alltrue":"",
"alterdot":"",
"amax":"最大値",
"amin":"最小値",
"angle":"",
"any":"",
"append":"挿入",
"apply_along_axis":"",
"apply_over_axes":"",
"arange":"",
"arccos":"",
"arccosh":"",
"arcsin":"",
"arcsinh":"",
"arctan":"",
"arctan2":"",
"arctanh":"",
"argmax":"",
"argmin":"",
"argsort":"",
"argwhere":"",
"around":"",
"array":"配列",
"array2string":"配列を文字に変換",
"array_equal":"",
"array_equiv":"",
"array_repr":"",
"array_split":"",
"array_str":"",
"asanyarray":"",
"asarray":"",
"asarray_chkfinite":"",
"ascontiguousarray":"",
"asfarray":"",
"asfortranarray":"",
"asmatrix":"",
"asscalar":"",
"atleast_1d":"",
"atleast_2d":"",
"atleast_3d":"",
"average":"",
"bartlett":"",
"base_repr":"",
"bench":"",
"binary_repr":"",
"bincount":"",
"bitwise_and":"",
"bitwise_not":"",
"bitwise_or":"",
"bitwise_xor":"",
"blackman":"",
"bmat":"",
"bool":"",
"bool8":"",
"bool_":"",
"broadcast":"",
"broadcast_arrays":"",
"byte":"バイト型",
"byte_bounds":"",
"bytes0":"",
"bytes_":"",
"c_":"",
"can_cast":"",
"cast":"",
"cdouble":"",
"ceil":"",
"cfloat":"",
"char":"",
"character":"",
"chararray":"",
"choose":"",
"clip":"",
"clongdouble":"",
"clongfloat":"",
"column_stack":"",
"common_type":"",
"compare_chararrays":"",
"compat":"",
"complex":"",
"complex128":"",
"complex192":"",
"complex64":"",
"complex_":"",
"complexfloating":"",
"compress":"",
"concatenate":"",
"conj":"",
"conjugate":"",
"convolve":"",
"copy":"コピー",
"copysign":"",
"core":"",
"corrcoef":"",
"correlate":"",
"cos":"コサイン",
"cosh":"",
"count_nonzero":"",
"cov":"共分散行列",
"cross":"",
"csingle":"",
"ctypeslib":"",
"cumprod":"",
"cumproduct":"",
"cumsum":"",
"datetime64":"",
"datetime_":"",
"datetime_data":"",
"deg2rad":"",
"degrees":"",
"delete":"",
"deprecate":"",
"deprecate_with_doc":"",
"diag":"",
"diag_indices":"",
"diag_indices_from":"",
"diagflat":"",
"diagonal":"",
"diff":"",
"digitize":"",
"disp":"",
"divide":"除算",
"dot":"行列積",
"double":"",
"dsplit":"",
"dstack":"",
"dtype":"",
"e":"ネイピア数",
"e":"自然対数の底",
"ediff1d":"",
"einsum":"",
"emath":"",
"empty":"",
"empty_like":"",
"equal":"",
"errstate":"",
"exp":"",
"exp2":"",
"expand_dims":"",
"expm1":"",
"extract":"",
"eye":"",
"fabs":"",
"fastCopyAndTranspose":"",
"fft":"",
"fill_diagonal":"",
"find_common_type":"",
"finfo":"",
"fix":"",
"flatiter":"",
"flatnonzero":"",
"flexible":"",
"fliplr":"",
"flipud":"",
"float":"浮動小数点数",
"float16":"浮動小数点数16bit",
"float32":"浮動小数点数32bit",
"float64":"浮動小数点数64bit",
"float96":"浮動小数点数96bit",
"float_":"浮動小数点数",
"floating":"",
"floor":"",
"floor_divide":"",
"fmax":"",
"fmin":"",
"fmod":"",
"format_parser":"",
"frexp":"",
"frombuffer":"",
"fromfile":"",
"fromfunction":"",
"fromiter":"",
"frompyfunc":"",
"fromregex":"",
"fromstring":"",
"fv":"",
"generic":"",
"genfromtxt":"",
"get_array_wrap":"",
"get_include":"",
"get_numarray_include":"",
"get_printoptions":"",
"getbufsize":"",
"geterr":"",
"geterrcall":"",
"geterrobj":"",
"gradient":"",
"greater":"",
"greater_equal":"",
"half":"",
"hamming":"",
"hanning":"",
"histogram":"",
"histogram2d":"",
"histogramdd":"",
"hsplit":"",
"hstack":"",
"hypot":"",
"i0":"",
"identity":"",
"iinfo":"",
"imag":"",
"in1d":"",
"index_exp":"",
"indices":"",
"inexact":"",
"inf":"無限大",
"info":"",
"infty":"",
"inner":"",
"insert":"",
"int":"整数",
"int0":"整数",
"int16":"整数16bit",
"int32":"整数32bit",
"int64":"整数64bit",
"int8":"整数8bit",
"int_":"整数",
"int_asbuffer":"",
"intc":"",
"integer":"",
"interp":"",
"intersect1d":"",
"intp":"",
"invert":"",
"ipmt":"",
"irr":"",
"iscomplex":"複素数であるか",
"iscomplexobj":"複素数オブジェクトであるか",
"isfinite":"",
"isfortran":"",
"isinf":"無限大であるか",
"isnan":"数字ではないか",
"isneginf":"負の無限大であるか",
"isposinf":"正の無限大であるか",
"isreal":"",
"isrealobj":"",
"isscalar":"",
"issctype":"",
"issubclass_":"",
"issubdtype":"",
"issubsctype":"",
"iterable":"",
"ix_":"",
"kaiser":"",
"kron":"",
"ldexp":"",
"left_shift":"",
"less":"",
"less_equal":"",
"lexsort":"",
"lib":"",
"linalg":"",
"linspace":"",
"little_endian":"",
"load":"",
"loads":"",
"loadtxt":"",
"log":"",
"log10":"",
"log1p":"",
"log2":"",
"logaddexp":"",
"logaddexp2":"",
"logical_and":"",
"logical_not":"",
"logical_or":"",
"logical_xor":"",
"logspace":"",
"long":"",
"longcomplex":"",
"longdouble":"",
"longfloat":"",
"longlong":"",
"lookfor":"",
"ma":"",
"mafromtxt":"",
"mask_indices":"",
"mat":"",
"math":"",
"matrix":"行列",
"matrixlib":"",
"max":"最大値",
"maximum":"",
"maximum_sctype":"",
"may_share_memory":"",
"mean":"",
"median":"",
"memmap":"",
"meshgrid":"",
"mgrid":"",
"min":"最小値",
"min_scalar_type":"",
"minimum":"",
"mintypecode":"",
"mirr":"",
"mod":"",
"modf":"",
"msort":"",
"multiply":"乗算",
"nan":"NaN",
"nan_to_num":"NaNを数値化",
"nanargmax":"",
"nanargmin":"",
"nanmax":"",
"nanmin":"",
"nansum":"",
"nbytes":"",
"ndarray":"",
"ndenumerate":"",
"ndfromtxt":"",
"ndim":"",
"ndindex":"",
"nditer":"",
"negative":"",
"nested_iters":"",
"newaxis":"",
"nextafter":"",
"nonzero":"",
"not_equal":"",
"nper":"",
"npv":"",
"number":"",
"obj2sctype":"",
"object":"",
"object0":"",
"object_":"",
"ogrid":"",
"ones":"",
"ones_like":"",
"outer":"",
"packbits":"",
"percentile":"",
"pi":"円周率",
"piecewise":"",
"pkgload":"",
"place":"",
"pmt":"",
"poly":"",
"poly1d":"",
"polyadd":"",
"polyder":"",
"polydiv":"",
"polyfit":"",
"polyint":"",
"polymul":"",
"polynomial":"",
"polysub":"",
"polyval":"",
"power":"",
"ppmt":"",
"prod":"",
"product":"",
"promote_types":"",
"ptp":"",
"put":"",
"putmask":"",
"pv":"",
"r_":"",
"rad2deg":"",
"radians":"",
"random":"乱数モジュール",
"rank":"",
"rate":"",
"ravel":"",
"ravel_multi_index":"",
"real":"",
"real_if_close":"",
"rec":"",
"recarray":"",
"recfromcsv":"",
"recfromtxt":"",
"reciprocal":"",
"record":"",
"remainder":"",
"repeat":"",
"require":"",
"reshape":"",
"resize":"",
"restoredot":"",
"result_type":"",
"right_shift":"",
"rint":"",
"roll":"",
"rollaxis":"",
"roots":"",
"rot90":"",
"round":"",
"round_":"",
"row_stack":"",
"s_":"",
"safe_eval":"",
"save":"",
"savetxt":"",
"savez":"",
"savez_compressed":"",
"sctype2char":"",
"sctypeDict":"",
"sctypeNA":"",
"sctypes":"",
"searchsorted":"",
"select":"",
"set_numeric_ops":"",
"set_printoptions":"",
"set_string_function":"",
"setbufsize":"",
"setdiff1d":"",
"seterr":"",
"seterrcall":"",
"seterrobj":"",
"setxor1d":"",
"shape":"",
"short":"",
"show_config":"",
"sign":"",
"signbit":"",
"signedinteger":"",
"sin":"",
"sinc":"",
"single":"",
"singlecomplex":"",
"sinh":"",
"size":"",
"sometrue":"",
"sort":"",
"sort_complex":"",
"source":"",
"spacing":"",
"split":"",
"sqrt":"",
"square":"",
"squeeze":"",
"std":"",
"str":"",
"str0":"",
"str_":"",
"string_":"",
"subtract":"減算",
"sum":"合計",
"swapaxes":"",
"take":"",
"tan":"タンジェント",
"tanh":"",
"tensordot":"",
"test":"",
"testing":"",
"tile":"",
"timedelta64":"",
"timedelta_":"",
"timeinteger":"",
"trace":"",
"transpose":"",
"trapz":"",
"tri":"",
"tril":"",
"tril_indices":"",
"tril_indices_from":"",
"trim_zeros":"",
"triu":"",
"triu_indices":"",
"triu_indices_from":"",
"true_divide":"",
"trunc":"",
"typeDict":"",
"typeNA":"",
"typecodes":"",
"typename":"",
"ubyte":"",
"ufunc":"",
"uint":"符号なし整数",
"uint0":"符号なし整数",
"uint16":"符号なし整数16bit",
"uint32":"符号なし整数32bit",
"uint64":"符号なし整数64bit",
"uint8":"符号なし整数8bit",
"uintc":"",
"uintp":"",
"ulonglong":"",
"unicode":"",
"unicode_":"",
"union1d":"",
"unique":"",
"unpackbits":"",
"unravel_index":"",
"unsignedinteger":"符号なし整数",
"unwrap":"",
"ushort":"",
"vander":"",
"var":"",
"vdot":"",
"vectorize":"",
"version":"",
"void":"",
"void0":"",
"vsplit":"",
"vstack":"",
"where":"",
"who":"",
"zeros":"",
"zeros_like":""
}
Numpy_matrix用日本語={
"A":"",
"A1":"",
"H":"",
"I":"",
"T":"転置行列",
"all":"",
"any":"",
"argmax":"",
"argmin":"",
"argsort":"",
"astype":"",
"base":"",
"byteswap":"",
"choose":"",
"clip":"",
"compress":"",
"conj":"",
"conjugate":"",
"copy":"",
"ctypes":"",
"cumprod":"",
"cumsum":"",
"data":"",
"diagonal":"",
"dot":"",
"dtype":"データ型",
"dump":"",
"dumps":"",
"fill":"",
"flags":"",
"flat":"",
"flatten":"",
"getA":"",
"getA1":"",
"getH":"",
"getI":"",
"getT":"",
"getfield":"",
"imag":"",
"item":"",
"itemset":"",
"itemsize":"",
"max":"最大値",
"mean":"",
"min":"",
"nbytes":"",
"ndim":"",
"newbyteorder":"",
"nonzero":"",
"prod":"",
"ptp":"",
"put":"",
"ravel":"",
"real":"",
"repeat":"",
"reshape":"",
"resize":"",
"round":"",
"searchsorted":"",
"setasflat":"",
"setfield":"",
"setflags":"",
"shape":"行数、列数",
"size":"",
"sort":"",
"squeeze":"",
"std":"",
"strides":"",
"sum":"",
"swapaxes":"",
"take":"",
"tofile":"",
"tolist":"",
"tostring":"",
"trace":"",
"transpose":"転置",
"var":"",
"view":""
}
for key in Numpy用日本語:
    if Numpy用日本語[key]:
        exec("numpy.%s = numpy.%s" % (Numpy用日本語[key],key) )
for key in Numpy_matrix用日本語:
    if Numpy_matrix用日本語[key]:
        exec("numpy.matrix.%s = numpy.matrix.%s" % (Numpy_matrix用日本語[key],key) )

if __name__ == "__main__":
    pass
