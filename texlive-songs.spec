Name:		texlive-songs
Version:	51494
Release:	2
Summary:	Produce song books for church or fellowship
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/songs
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/songs.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/songs.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/songs.source.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/songs
%doc %{_texmfdistdir}/doc/latex/songs
#- source
%doc %{_texmfdistdir}/source/latex/songs

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
