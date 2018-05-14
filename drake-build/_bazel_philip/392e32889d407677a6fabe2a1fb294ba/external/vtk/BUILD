# -*- python -*-
cc_library(
    name = "vtkCommonColor",
    srcs = [],
    hdrs = [],
    includes = [],
    linkopts = ["-L/usr/local/opt/vtk@8.0/lib", "-lvtkCommonColor-8.0"],
    visibility = ["//visibility:private"],
    deps = [":vtkCommonCore", ":vtkCommonDataModel"],
)
    
cc_library(
    name = "vtkCommonComputationalGeometry",
    srcs = [],
    hdrs = [],
    includes = [],
    linkopts = ["-L/usr/local/opt/vtk@8.0/lib", "-lvtkCommonComputationalGeometry-8.0"],
    visibility = ["//visibility:private"],
    deps = [":vtkCommonCore", ":vtkCommonDataModel"],
)
    
cc_library(
    name = "vtkCommonCore",
    srcs = [],
    hdrs = ["include/vtk-8.0/vtkABI.h", "include/vtk-8.0/vtkAbstractArray.h", "include/vtk-8.0/vtkAOSDataArrayTemplate.h", "include/vtk-8.0/vtkAOSDataArrayTemplate.txx", "include/vtk-8.0/vtkArrayIterator.h", "include/vtk-8.0/vtkArrayIteratorTemplate.h", "include/vtk-8.0/vtkArrayIteratorTemplate.txx", "include/vtk-8.0/vtkAtomic.h", "include/vtk-8.0/vtkAtomicTypeConcepts.h", "include/vtk-8.0/vtkAtomicTypes.h", "include/vtk-8.0/vtkAutoInit.h", "include/vtk-8.0/vtkBuffer.h", "include/vtk-8.0/vtkCollection.h", "include/vtk-8.0/vtkCommand.h", "include/vtk-8.0/vtkCommonCoreModule.h", "include/vtk-8.0/vtkConfigure.h", "include/vtk-8.0/vtkDataArray.h", "include/vtk-8.0/vtkDebugLeaksManager.h", "include/vtk-8.0/vtkGenericDataArray.h", "include/vtk-8.0/vtkGenericDataArray.txx", "include/vtk-8.0/vtkGenericDataArrayLookupHelper.h", "include/vtk-8.0/vtkIdList.h", "include/vtk-8.0/vtkIdTypeArray.h", "include/vtk-8.0/vtkIndent.h", "include/vtk-8.0/vtkIntArray.h", "include/vtk-8.0/vtkIOStream.h", "include/vtk-8.0/vtkMath.h", "include/vtk-8.0/vtkMathConfigure.h", "include/vtk-8.0/vtkNew.h", "include/vtk-8.0/vtkObject.h", "include/vtk-8.0/vtkObjectBase.h", "include/vtk-8.0/vtkObjectFactory.h", "include/vtk-8.0/vtkOStreamWrapper.h", "include/vtk-8.0/vtkOStrStreamWrapper.h", "include/vtk-8.0/vtkPoints.h", "include/vtk-8.0/vtkSetGet.h", "include/vtk-8.0/vtkSmartPointer.h", "include/vtk-8.0/vtkSmartPointerBase.h", "include/vtk-8.0/vtkStdString.h", "include/vtk-8.0/vtkSystemIncludes.h", "include/vtk-8.0/vtkTimeStamp.h", "include/vtk-8.0/vtkType.h", "include/vtk-8.0/vtkTypeTraits.h", "include/vtk-8.0/vtkUnicodeString.h", "include/vtk-8.0/vtkUnsignedCharArray.h", "include/vtk-8.0/vtkVariant.h", "include/vtk-8.0/vtkVariantCast.h", "include/vtk-8.0/vtkVariantInlineOperators.h", "include/vtk-8.0/vtkVersion.h", "include/vtk-8.0/vtkVersionMacros.h", "include/vtk-8.0/vtkWeakPointer.h", "include/vtk-8.0/vtkWeakPointerBase.h", "include/vtk-8.0/vtkWin32Header.h", "include/vtk-8.0/vtkWindow.h", "include/vtk-8.0/vtkWrappingHints.h"],
    includes = ["include/vtk-8.0"],
    linkopts = ["-L/usr/local/opt/vtk@8.0/lib", "-lvtkCommonCore-8.0"],
    visibility = ["//visibility:public"],
    deps = [":vtkkwiml", ":vtksys"],
)
    
cc_library(
    name = "vtkCommonDataModel",
    srcs = [],
    hdrs = ["include/vtk-8.0/vtkAbstractCellLinks.h", "include/vtk-8.0/vtkCell.h", "include/vtk-8.0/vtkCellArray.h", "include/vtk-8.0/vtkCellData.h", "include/vtk-8.0/vtkCellLinks.h", "include/vtk-8.0/vtkCellType.h", "include/vtk-8.0/vtkCellTypes.h", "include/vtk-8.0/vtkCommonDataModelModule.h", "include/vtk-8.0/vtkDataObject.h", "include/vtk-8.0/vtkDataSet.h", "include/vtk-8.0/vtkDataSetAttributes.h", "include/vtk-8.0/vtkFieldData.h", "include/vtk-8.0/vtkImageData.h", "include/vtk-8.0/vtkPointSet.h", "include/vtk-8.0/vtkPolyData.h", "include/vtk-8.0/vtkRect.h", "include/vtk-8.0/vtkStructuredData.h", "include/vtk-8.0/vtkVector.h"],
    includes = ["include/vtk-8.0"],
    linkopts = ["-L/usr/local/opt/vtk@8.0/lib", "-lvtkCommonDataModel-8.0"],
    visibility = ["//visibility:public"],
    deps = [":vtkCommonCore", ":vtkCommonMath", ":vtkCommonMisc", ":vtkCommonSystem", ":vtkCommonTransforms"],
)
    
cc_library(
    name = "vtkCommonExecutionModel",
    srcs = [],
    hdrs = ["include/vtk-8.0/vtkAlgorithm.h", "include/vtk-8.0/vtkCommonExecutionModelModule.h", "include/vtk-8.0/vtkImageAlgorithm.h", "include/vtk-8.0/vtkPolyDataAlgorithm.h"],
    includes = ["include/vtk-8.0"],
    linkopts = ["-L/usr/local/opt/vtk@8.0/lib", "-lvtkCommonExecutionModel-8.0"],
    visibility = ["//visibility:public"],
    deps = [":vtkCommonCore", ":vtkCommonDataModel", ":vtkCommonMisc"],
)
    
cc_library(
    name = "vtkCommonMath",
    srcs = [],
    hdrs = ["include/vtk-8.0/vtkCommonMathModule.h", "include/vtk-8.0/vtkMatrix4x4.h", "include/vtk-8.0/vtkTuple.h"],
    includes = ["include/vtk-8.0"],
    linkopts = ["-L/usr/local/opt/vtk@8.0/lib", "-lvtkCommonMath-8.0"],
    visibility = ["//visibility:public"],
    deps = [":vtkCommonCore"],
)
    
cc_library(
    name = "vtkCommonMisc",
    srcs = [],
    hdrs = [],
    includes = [],
    linkopts = ["-L/usr/local/opt/vtk@8.0/lib", "-lvtkCommonMisc-8.0"],
    visibility = ["//visibility:private"],
    deps = [":vtkCommonCore", ":vtkCommonMath"],
)
    
cc_library(
    name = "vtkCommonSystem",
    srcs = [],
    hdrs = [],
    includes = [],
    linkopts = ["-L/usr/local/opt/vtk@8.0/lib", "-lvtkCommonSystem-8.0"],
    visibility = ["//visibility:private"],
    deps = [":vtkCommonCore"],
)
    
cc_library(
    name = "vtkCommonTransforms",
    srcs = [],
    hdrs = ["include/vtk-8.0/vtkAbstractTransform.h", "include/vtk-8.0/vtkCommonTransformsModule.h", "include/vtk-8.0/vtkHomogeneousTransform.h", "include/vtk-8.0/vtkLinearTransform.h", "include/vtk-8.0/vtkTransform.h"],
    includes = ["include/vtk-8.0"],
    linkopts = ["-L/usr/local/opt/vtk@8.0/lib", "-lvtkCommonTransforms-8.0"],
    visibility = ["//visibility:public"],
    deps = [":vtkCommonCore", ":vtkCommonMath"],
)
    
cc_library(
    name = "vtkDICOMParser",
    srcs = [],
    hdrs = [],
    includes = [],
    linkopts = ["-L/usr/local/opt/vtk@8.0/lib", "-lvtkDICOMParser-8.0"],
    visibility = ["//visibility:private"],
    deps = [":vtksys"],
)
    
cc_library(
    name = "vtkFiltersCore",
    srcs = [],
    hdrs = ["include/vtk-8.0/vtkCleanPolyData.h", "include/vtk-8.0/vtkFiltersCoreModule.h"],
    includes = ["include/vtk-8.0"],
    linkopts = ["-L/usr/local/opt/vtk@8.0/lib", "-lvtkFiltersCore-8.0"],
    visibility = ["//visibility:private"],
    deps = [":vtkCommonCore", ":vtkCommonDataModel", ":vtkCommonExecutionModel", ":vtkCommonMisc"],
)
    
cc_library(
    name = "vtkFiltersGeometry",
    srcs = [],
    hdrs = [],
    includes = [],
    linkopts = ["-L/usr/local/opt/vtk@8.0/lib", "-lvtkFiltersGeometry-8.0"],
    visibility = ["//visibility:private"],
    deps = [":vtkCommonCore", ":vtkCommonDataModel", ":vtkCommonExecutionModel"],
)
    
cc_library(
    name = "vtkFiltersGeneral",
    srcs = [],
    hdrs = ["include/vtk-8.0/vtkFiltersGeneralModule.h", "include/vtk-8.0/vtkTransformPolyDataFilter.h"],
    includes = ["include/vtk-8.0"],
    linkopts = ["-L/usr/local/opt/vtk@8.0/lib", "-lvtkFiltersGeneral-8.0"],
    visibility = ["//visibility:public"],
    deps = [":vtkCommonComputationalGeometry", ":vtkCommonCore", ":vtkCommonDataModel", ":vtkCommonExecutionModel", ":vtkCommonMisc", ":vtkFiltersCore"],
)
    
cc_library(
    name = "vtkFiltersSources",
    srcs = [],
    hdrs = ["include/vtk-8.0/vtkCubeSource.h", "include/vtk-8.0/vtkCylinderSource.h", "include/vtk-8.0/vtkFiltersSourcesModule.h", "include/vtk-8.0/vtkPlaneSource.h", "include/vtk-8.0/vtkSphereSource.h"],
    includes = ["include/vtk-8.0"],
    linkopts = ["-L/usr/local/opt/vtk@8.0/lib", "-lvtkFiltersSources-8.0"],
    visibility = ["//visibility:public"],
    deps = [":vtkCommonDataModel", ":vtkCommonExecutionModel", ":vtkFiltersCore", ":vtkFiltersGeneral"],
)
    
cc_library(
    name = "vtkIOCore",
    srcs = [],
    hdrs = ["include/vtk-8.0/vtkAbstractPolyDataReader.h", "include/vtk-8.0/vtkIOCoreModule.h"],
    includes = ["include/vtk-8.0"],
    linkopts = ["-L/usr/local/opt/vtk@8.0/lib", "-lvtkIOCore-8.0"],
    visibility = ["//visibility:public"],
    deps = [":vtkCommonCore", ":vtkCommonExecutionModel", "@liblz4"],
)
    
cc_library(
    name = "vtkIOXMLParser",
    srcs = [],
    hdrs = [],
    includes = [],
    linkopts = ["-L/usr/local/opt/vtk@8.0/lib", "-lvtkIOXMLParser-8.0"],
    visibility = ["//visibility:private"],
    deps = [":vtkCommonCore", ":vtkCommonDataModel", ":vtkIOCore", ":vtksys", "@expat"],
)
    
cc_library(
    name = "vtkIOXML",
    srcs = [],
    hdrs = ["include/vtk-8.0/vtkIOXMLModule.h", "include/vtk-8.0/vtkXMLDataReader.h", "include/vtk-8.0/vtkXMLPolyDataReader.h", "include/vtk-8.0/vtkXMLReader.h", "include/vtk-8.0/vtkXMLUnstructuredDataReader.h"],
    includes = ["include/vtk-8.0"],
    linkopts = ["-L/usr/local/opt/vtk@8.0/lib", "-lvtkIOXML-8.0"],
    visibility = ["//visibility:public"],
    deps = [":vtkCommonCore", ":vtkCommonDataModel", ":vtkCommonExecutionModel", ":vtkIOCore", ":vtkIOXMLParser", ":vtksys"],
)
    
cc_library(
    name = "vtkIOGeometry",
    srcs = [],
    hdrs = ["include/vtk-8.0/vtkIOGeometryModule.h", "include/vtk-8.0/vtkOBJReader.h"],
    includes = ["include/vtk-8.0"],
    linkopts = ["-L/usr/local/opt/vtk@8.0/lib", "-lvtkIOGeometry-8.0"],
    visibility = ["//visibility:public"],
    deps = [":vtkCommonDataModel", ":vtkCommonExecutionModel", ":vtkIOCore", ":vtkIOLegacy"],
)
    
cc_library(
    name = "vtkIOImage",
    srcs = [],
    hdrs = ["include/vtk-8.0/vtkImageExport.h", "include/vtk-8.0/vtkImageReader2.h", "include/vtk-8.0/vtkImageWriter.h", "include/vtk-8.0/vtkIOImageModule.h", "include/vtk-8.0/vtkPNGReader.h", "include/vtk-8.0/vtkPNGWriter.h"],
    includes = ["include/vtk-8.0"],
    linkopts = ["-L/usr/local/opt/vtk@8.0/lib", "-lvtkIOImage-8.0"],
    visibility = ["//visibility:public"],
    deps = [":vtkCommonCore", ":vtkCommonExecutionModel", ":vtkDICOMParser", ":vtkmetaio", "@libpng", "@zlib"],
)
    
cc_library(
    name = "vtkIOImport",
    srcs = [],
    hdrs = ["include/vtk-8.0/vtkImporter.h", "include/vtk-8.0/vtkIOImportModule.h", "include/vtk-8.0/vtkOBJImporter.h"],
    includes = ["include/vtk-8.0"],
    linkopts = ["-L/usr/local/opt/vtk@8.0/lib", "-lvtkIOImport-8.0"],
    visibility = ["//visibility:public"],
    deps = [":vtkCommonCore", ":vtkCommonExecutionModel", ":vtkCommonMisc", ":vtkRenderingCore", ":vtksys"],
)
    
cc_library(
    name = "vtkIOLegacy",
    srcs = [],
    hdrs = [],
    includes = [],
    linkopts = ["-L/usr/local/opt/vtk@8.0/lib", "-lvtkIOLegacy-8.0"],
    visibility = ["//visibility:private"],
    deps = [":vtkCommonCore", ":vtkCommonDataModel", ":vtkCommonExecutionModel", ":vtkIOCore"],
)
    
cc_library(
    name = "vtkRenderingCore",
    srcs = [],
    hdrs = ["include/vtk-8.0/vtkAbstractMapper.h", "include/vtk-8.0/vtkAbstractMapper3D.h", "include/vtk-8.0/vtkActor.h", "include/vtk-8.0/vtkActorCollection.h", "include/vtk-8.0/vtkCamera.h", "include/vtk-8.0/vtkMapper.h", "include/vtk-8.0/vtkPolyDataMapper.h", "include/vtk-8.0/vtkProp.h", "include/vtk-8.0/vtkProp3D.h", "include/vtk-8.0/vtkPropCollection.h", "include/vtk-8.0/vtkProperty.h", "include/vtk-8.0/vtkRenderer.h", "include/vtk-8.0/vtkRenderingCoreModule.h", "include/vtk-8.0/vtkRenderWindow.h", "include/vtk-8.0/vtkTexture.h", "include/vtk-8.0/vtkViewport.h", "include/vtk-8.0/vtkVolume.h", "include/vtk-8.0/vtkVolumeCollection.h", "include/vtk-8.0/vtkWindowToImageFilter.h"],
    includes = ["include/vtk-8.0"],
    linkopts = ["-L/usr/local/opt/vtk@8.0/lib", "-lvtkRenderingCore-8.0"],
    visibility = ["//visibility:public"],
    deps = [":vtkCommonColor", ":vtkCommonCore", ":vtkCommonDataModel", ":vtkCommonExecutionModel", ":vtkCommonMath", ":vtkFiltersCore", ":vtkFiltersGeometry"],
)
    
cc_library(
    name = "vtkRenderingOpenGL2",
    srcs = [],
    hdrs = ["include/vtk-8.0/vtkOpenGLHelper.h", "include/vtk-8.0/vtkOpenGLPolyDataMapper.h", "include/vtk-8.0/vtkOpenGLRenderWindow.h", "include/vtk-8.0/vtkOpenGLTexture.h", "include/vtk-8.0/vtkRenderingOpenGL2Module.h", "include/vtk-8.0/vtkRenderingOpenGLConfigure.h", "include/vtk-8.0/vtkShader.h", "include/vtk-8.0/vtkShaderProgram.h", "include/vtk-8.0/vtkTextureObject.h"],
    includes = ["include/vtk-8.0"],
    linkopts = ["-L/usr/local/opt/vtk@8.0/lib", "-lvtkRenderingOpenGL2-8.0"],
    visibility = ["//visibility:public"],
    deps = [":vtkCommonCore", ":vtkCommonDataModel", ":vtkRenderingCore", "@glew"],
)
    
cc_library(
    name = "vtkkwiml",
    srcs = [],
    hdrs = ["include/vtk-8.0/vtk_kwiml.h", "include/vtk-8.0/vtkkwiml/abi.h", "include/vtk-8.0/vtkkwiml/int.h"],
    includes = ["include/vtk-8.0"],
    linkopts = [],
    visibility = ["//visibility:private"],
    deps = [],
)
    
cc_library(
    name = "vtkmetaio",
    srcs = [],
    hdrs = [],
    includes = [],
    linkopts = ["-L/usr/local/opt/vtk@8.0/lib", "-lvtkmetaio-8.0"],
    visibility = ["//visibility:private"],
    deps = ["@zlib"],
)
    
cc_library(
    name = "vtksys",
    srcs = [],
    hdrs = [],
    includes = [],
    linkopts = ["-L/usr/local/opt/vtk@8.0/lib", "-lvtksys-8.0"],
    visibility = ["//visibility:private"],
    deps = [],
)
    
filegroup(
    name = "vtk",
    srcs = glob(["**/*"], exclude=["BUILD", "WORKSPACE"]),
    visibility = ["//visibility:public"],
)

load("@drake//tools/install:install.bzl", "install_files")
install_files(
    name = "install",
    dest = ".",
    files = [],
    visibility = ["//visibility:public"],
)
