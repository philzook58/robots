# -*- python -*-

package(default_visibility = ["//visibility:public"])

cc_library(
    name = "libprotobuf",
    srcs = [],
    hdrs = glob(["include/**"]) + [],
    copts = [],
    defines = ["_THREAD_SAFE"],
    includes = ["include/_usr_local_Cellar_protobuf_3.5.1_1_include"],
    linkopts = ["-Wl,-rpath /usr/local/Cellar/protobuf/3.5.1_1/lib -L/usr/local/Cellar/protobuf/3.5.1_1/lib", "-lprotobuf", "-D_THREAD_SAFE"],
    deps = [],
)
