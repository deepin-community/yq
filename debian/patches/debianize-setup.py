--- a/setup.py
+++ b/setup.py
@@ -12,10 +12,6 @@ setup(
     description="Command-line YAML/XML processor - jq wrapper for YAML/XML documents",
     long_description=open("README.rst").read(),
     python_requires=">=3.6",
-    use_scm_version={
-        "write_to": "yq/version.py",
-    },
-    setup_requires=["setuptools_scm >= 3.4.3"],
     install_requires=[
         "PyYAML >= 5.3.1",
         "xmltodict >= 0.11.0",
