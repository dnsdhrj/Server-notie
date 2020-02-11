with import <nixpkgs> {};

python37Packages.buildPythonApplication {
  pname = "notie";
  version = "1.0";
  src = lib.cleanSource ./.;
  propagatedBuildInputs = callPackage ./requirements.nix {};
  doCheck = false;
}

