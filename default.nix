{ pkgs ? import <nixpkgs> {}, pythonPackages ? pkgs.python35Packages }:
rec {
  sphobjinv = pythonPackages.callPackage ./sphobjinv.nix {};
  sphinxcontrib-domaintools = pythonPackages.callPackage ./sphinxcontrib-domaintools.nix {};
  sphinxcontrib-haddock = pythonPackages.callPackage ./sphinxcontrib-haddock.nix { inherit sphobjinv sphinxcontrib-domaintools; };
}
