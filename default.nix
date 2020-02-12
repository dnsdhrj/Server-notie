with import <nixpkgs> {};

let
  
  # Actual Python package
  notieBarebone = python37Packages.buildPythonApplication {
    pname = "notie-barebone";
    version = "1.0";
    src = lib.cleanSource ./.;
    propagatedBuildInputs = callPackage ./requirements.nix {};
    doCheck = false;
  };

  # One-liners for convenience
  blackaddScript = writeShellScriptBin "blackadd" "function _blackadd() { notie-command blackadd $1; }; _blackadd";
  blackdelScript = writeShellScriptBin "blackdel" "function _blackdel() { notie-command blackdel $1; }; _blackdel";
  blacklistScript = writeShellScriptBin "blacklist" "notie-command blacklist";
  clearemailScript = writeShellScriptBin "clearemail" "notie-command clearemail";
  mclearScript = writeShellScriptBin "mclear" "clearemail";

in
stdenv.mkDerivation {
  name = "notie";
  src = notieBarebone;
  installPhase = ''
    cp -r . $out
    cp -r ${blackaddScript}/* $out
    cp -r ${blackdelScript}/* $out
    cp -r ${blacklistScript}/* $out
    cp -r ${clearemailScript}/* $out
    cp -r ${mclearScript}/* $out
  '';
}
