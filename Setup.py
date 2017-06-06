import os
import sys
from distutils.core import setup
import cx_Freeze
import matplotlib 
matplotlib.use('TkAgg')

base = "win32gui"

#os.environ['TCL_LIBRARY'] = r'D:\Anaconda\envs\py34\tcl\tcl8.6'
#os.environ['TK_LIBRARY'] = r'D:\Anaconda\envs\py34\tcl\tk8.6'

executable = [
    cx_Freeze.Executable("Dynamic Plotting Animate.py", base = base, icon="Icons8-Halloween-Cat.ico")
]

build_exe_options = {"includes":["numpy.core._methods", "numpy.lib.format", "matplotlib.backends.backend_tkagg"],
                     "packages": ["tkinter"],
                     "include_files":[(matplotlib.get_data_path(), "mpl-data"), 
                     									("D:\\Anaconda\\envs\\py34\\tcl\\tcl8.6", "tcl8.6"),
                     									("D:\\Anaconda\\envs\\py34\\tcl\\tk8.6", "tk8.6"),
                     									("D:\\Anaconda\\envs\\py34\\lib\\site-packages\\numpy", "numpy"),
                     									("D:\\Anaconda\\envs\\py34\\lib\\site-packages\\matplotlib", "matplotlib"),
                     									("D:\\Anaconda\\envs\\py34\\Lib\\site-packages\\mkl\\__init__.py","__init__.py"),
                     									("D:\\Anaconda\\envs\\py34\\Lib\\site-packages\\mkl\\__pycache__\\__init__.cpython-34.pyc","_init__.cpython-34.pyc"),
                     									("D:\\Anaconda\\envs\\py34\\Lib\\site-packages\\mkl\\__pycache__\\test.cpython-34.pyc","test.cpython-34.pyc"),
                     									("D:\\Anaconda\\envs\\py34\\Lib\\site-packages\\mkl\\service.pyd","service.pyd"),
                     									("D:\\Anaconda\\envs\\py34\\Lib\\site-packages\\mkl\\test.py","test.py"),                   									
                     									("D:/Anaconda/envs/py34/Library/bin/cilkrts20.dll","cilkrts20.dll"),
                     									("D:/Anaconda/envs/py34/Library/bin/ifdlg100.dll","ifdlg100.dll"),
                     									("D:/Anaconda/envs/py34/Library/bin/libchkp.dll","libchkp.dll"),
                     									("D:/Anaconda/envs/py34/Library/bin/libicaf.dll","libicaf.dll"),
                     									("D:/Anaconda/envs/py34/Library/bin/libifcoremd.dll","libifcoremd.dll"),
                     									("D:/Anaconda/envs/py34/Library/bin/libifcoremdd.dll","libifcoremdd.dll"),
                     									("D:/Anaconda/envs/py34/Library/bin/libifcorert.dll","libifcorert.dll"),
                     									("D:/Anaconda/envs/py34/Library/bin/libifcorertd.dll","libifcorertd.dll"),
                     									("D:/Anaconda/envs/py34/Library/bin/libifportmd.dll","libifportmd.dll"),
                     									("D:/Anaconda/envs/py34/Library/bin/libimalloc.dll","libimalloc.dll"),
                     									("D:/Anaconda/envs/py34/Library/bin/libiomp5md.dll","libiomp5md.dll"),
                     									("D:/Anaconda/envs/py34/Library/bin/libiompstubs5md.dll","libiompstubs5md.dll"),
                     									("D:/Anaconda/envs/py34/Library/bin/libmmd.dll","libmmd.dll"),
                     									("D:/Anaconda/envs/py34/Library/bin/libmmdd.dll","libmmdd.dll"),
                     									("D:/Anaconda/envs/py34/Library/bin/libmpx.dll","libmpx.dll"),
                     									("D:/Anaconda/envs/py34/Library/bin/liboffload.dll","liboffload.dll"),
                     									("D:/Anaconda/envs/py34/Library/bin/mkl_avx.dll","mkl_avx.dll"),
                     									("D:/Anaconda/envs/py34/Library/bin/mkl_avx2.dll","mkl_avx2.dll"),
                     									("D:/Anaconda/envs/py34/Library/bin/mkl_avx512.dll","mkl_avx512.dll"),
                     									("D:/Anaconda/envs/py34/Library/bin/mkl_avx512_mic.dll","mkl_avx512_mic.dll"),
                     									("D:/Anaconda/envs/py34/Library/bin/mkl_core.dll","mkl_core.dll"),
                     									("D:/Anaconda/envs/py34/Library/bin/mkl_def.dll","mkl_def.dll"),
                     									("D:/Anaconda/envs/py34/Library/bin/mkl_intel_thread.dll","mkl_intel_thread.dll"),
                     									("D:/Anaconda/envs/py34/Library/bin/mkl_mc.dll","mkl_mc.dll"),
                     									("D:/Anaconda/envs/py34/Library/bin/mkl_mc3.dll","mkl_mc3.dll"),
                     									("D:/Anaconda/envs/py34/Library/bin/mkl_msg.dll","mkl_msg.dll"),
                     									("D:/Anaconda/envs/py34/Library/bin/mkl_rt.dll","mkl_rt.dll"),
                     									("D:/Anaconda/envs/py34/Library/bin/mkl_sequential.dll","mkl_sequential.dll"),
                     									("D:/Anaconda/envs/py34/Library/bin/mkl_tbb_thread.dll","mkl_tbb_thread.dll"),
                     									("D:/Anaconda/envs/py34/Library/bin/mkl_vml_avx.dll","mkl_vml_avx.dll"),
                     									("D:/Anaconda/envs/py34/Library/bin/mkl_vml_avx2.dll","mkl_vml_avx2.dll"),
                     									("D:/Anaconda/envs/py34/Library/bin/mkl_vml_avx512.dll","mkl_vml_avx512.dll"),
                     									("D:/Anaconda/envs/py34/Library/bin/mkl_vml_avx512_mic.dll","mkl_vml_avx512_mic.dll"),
                     									("D:/Dynamic Plotting/ffmpeg","ffmpeg")
                     								 ],
                     }

cx_Freeze.setup(
    name = "Dynamic Plotting",
    options = {"build_exe": build_exe_options},
    version = "1.0",
    description = "standalone information plotter",
    author="Kun-Hao Yeh",
    executables = executable
)