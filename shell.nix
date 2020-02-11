with import <nixpkgs> {};

pkgs.mkShell rec {
  buildInputs = [ python37 ] ++ import ./requirements.nix { inherit python37Packages; };
}
