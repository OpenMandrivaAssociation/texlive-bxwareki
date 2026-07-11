%global tl_name bxwareki
%global tl_revision 79312

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.8
Release:	%{tl_revision}.1
Summary:	Convert dates from Gregorian to Japanese calender
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/japanese/BX/bxwareki
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bxwareki.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bxwareki.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This LaTeX package provides commands to convert from the Gregorian
calendar (e. g. 2018/8/28) to the Japanese rendering of the Japanese
calendar (e. g. Heisei 30 nen 8 gatsu 28 nichi; actually with kanji
characters). You can choose whether the numbers are written in Western
numerals or kanji numerals. Note that the package only deals with dates
in the year 1873 or later, where the Japanese calendar is really a
Gregorian calendar with a different notation of years.

