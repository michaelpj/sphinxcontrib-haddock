{ pkgs ? import <nixpkgs> {} }:
rec {
  sphobjinv = pkgs.python35.pkgs.callPackage ./sphobjinv.nix {};
  sphinxcontrib-domaintools = pkgs.python35.pkgs.callPackage ./sphinxcontrib-domaintools.nix {};
  sphinxcontrib-haddock = pkgs.python35.pkgs.callPackage ./sphinxcontrib-haddock.nix { inherit sphobjinv sphinxcontrib-domaintools; };
}
