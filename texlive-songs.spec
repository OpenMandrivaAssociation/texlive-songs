# revision 30005
# category Package
# catalog-ctan /macros/latex/contrib/songs
# catalog-date 2012-04-22 21:38:25 +0200
# catalog-license gpl
# catalog-version 2.14
Name:		texlive-songs
Version:	2.14
Release:	3
Summary:	Produce song books for church or fellowship
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/songs
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/songs.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/songs.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/songs.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a means of producing beautiful song books
for church or fellowship. It offers: - a very easy chord-entry
syntax; - multiple modes (words-only; words+chords; slides;
handouts); - measure bars; - guitar tablatures; - automatic
transposition; - scripture quotations; - multiple indexes
(sorted by title, author, important lyrics, or scripture
references); and - projector-style output generation, for
interactive use. A set of example documents is provided.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/songs/songs.sty
%doc %{_texmfdistdir}/doc/latex/songs/Makefile
%doc %{_texmfdistdir}/doc/latex/songs/README
%doc %{_texmfdistdir}/doc/latex/songs/history.txt
%doc %{_texmfdistdir}/doc/latex/songs/license.txt
%doc %{_texmfdistdir}/doc/latex/songs/sample/Makefile
%doc %{_texmfdistdir}/doc/latex/songs/sample/chordbook.tex
%doc %{_texmfdistdir}/doc/latex/songs/sample/lyricbook.tex
%doc %{_texmfdistdir}/doc/latex/songs/sample/slidebook.tex
%doc %{_texmfdistdir}/doc/latex/songs/sample/songs.sbd
%doc %{_texmfdistdir}/doc/latex/songs/sample/transparencies.tex
%doc %{_texmfdistdir}/doc/latex/songs/songidx/Makefile
%doc %{_texmfdistdir}/doc/latex/songs/songidx/authidx.c
%doc %{_texmfdistdir}/doc/latex/songs/songidx/bible.can
%doc %{_texmfdistdir}/doc/latex/songs/songidx/catholic.can
%doc %{_texmfdistdir}/doc/latex/songs/songidx/chars.h
%doc %{_texmfdistdir}/doc/latex/songs/songidx/fileio.c
%doc %{_texmfdistdir}/doc/latex/songs/songidx/fileio.h
%doc %{_texmfdistdir}/doc/latex/songs/songidx/greek.can
%doc %{_texmfdistdir}/doc/latex/songs/songidx/protestant.can
%doc %{_texmfdistdir}/doc/latex/songs/songidx/scripidx.c
%doc %{_texmfdistdir}/doc/latex/songs/songidx/songidx.c
%doc %{_texmfdistdir}/doc/latex/songs/songidx/songidx.h
%doc %{_texmfdistdir}/doc/latex/songs/songidx/songsort.c
%doc %{_texmfdistdir}/doc/latex/songs/songidx/tanakh.can
%doc %{_texmfdistdir}/doc/latex/songs/songidx/titleidx.c
%doc %{_texmfdistdir}/doc/latex/songs/songidx/vsconfig.h
%doc %{_texmfdistdir}/doc/latex/songs/songs.pdf
#- source
%doc %{_texmfdistdir}/source/latex/songs/songs.dtx
%doc %{_texmfdistdir}/source/latex/songs/songs.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
