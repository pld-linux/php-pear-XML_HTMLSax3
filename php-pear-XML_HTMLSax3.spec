%define		_status		stable
%define		_pearname	XML_HTMLSax3
%include	/usr/lib/rpm/macros.php
Summary:	%{_pearname} - A SAX parser for HTML and other badly formed XML documents
Summary(pl.UTF-8):	%{_pearname} - parser SAX dla HTML-a i innych źle uformowanych dokumentów XML
Name:		php-pear-%{_pearname}
Version:	3.0.0
Release:	5
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	d6b96cbe3ae5f75e54a29ef0d82fd8b6
URL:		http://pear.php.net/package/XML_HTMLSax3
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(core) >= 4.0.5
Requires:	php-pear
Suggests:	php-pcre
Obsoletes:	php-pear-XML_HTMLSax3-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML_HTMLSax3 is a SAX based XML parser for badly formed XML documents,
such as HTML. The original code base was developed by Alexander Zhukov
and published at http://sourceforge.net/projects/phpshelve/. Alexander
kindly gave permission to modify the code and license for inclusion in
PEAR.

PEAR::XML_HTMLSax3 provides an API very similar to the native PHP XML
extension (http://www.php.net/xml), allowing handlers using one to be
easily adapted to the other. The key difference is HTMLSax will not
break on badly formed XML, allowing it to be used for parsing HTML
documents. Otherwise HTMLSax supports all the handlers available from
Expat except namespace and external entity handlers. Provides methods
for handling XML escapes as well as JSP/ASP opening and close tags.

Version 1.x introduced an API similar to the native SAX extension but
used a slow character by character approach to parsing.

Version 2.x has had it's internals completely overhauled to use a
Lexer, delivering performance *approaching* that of the native XML
extension, as well as a radically improved, modular design that makes
adding further functionality easy.

Version 3.x is about fine tuning the API, behaviour and providing a
mechanism to distinguish HTML "quirks" from badly formed HTML (later
functionality not yet implemented)

A big thanks to Jeff Moore (lead developer of WACT:
http://wact.sourceforge.net/) who's largely responsible for new
design, as well input from other members at Sitepoint's Advanced PHP
forums: http://www.sitepointforums.com/showthread.php?threadid=121246.

Thanks also to Marcus Baker (lead developer of SimpleTest:
http://www.lastcraft.com/simple_test.php) for sorting out the unit
tests.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
XML_HTMLSax3 to oparty na SAX parser XML-a dla źle uformowanych
dokumentów XML, takich jak HTML. Oryginalny kod bazowy został
stworzony przez Alexandra Zhukova i opublikowany pod
http://sourceforge.net/projects/phpshelve/. Alexander udzielił
pozwolenia na modyfikowanie tego kodu oraz licencji na dołączenie do
PEAR-a.

PEAR::XML_HTMLSax3 udostępnia API bardzo podobne do natywnego
rozszerzenia PHP XML (http://www.php.net/xml), co pozwala na łatwe
dostosowanie procedur obsługujących używających jednego API do
drugiego. Główna różnica polega na tym, że HTMLSax nie załamie się na
źle uformowanym XML-u, co pozwala na używanie go do przetwarzania
dokumentów HTML. Poza tym HTMLSax obsługuje wszystkie procedury
obsługi dostępne w Expacie z wyjątkiem procedur obsługi przestrzeni
nazw i zewnętrznych encji. Dostępne są metody do obsługi sekwencji
specjalnych XML, a także znaczników otwierających i zamykających
JSP/ASP.

Wersja 1.x wprowadziła API podobne do natywnego rozszerzenia SAX, ale
używała wolnego podejścia do przetwarzania (znak po znaku).

Wersja 2.x miała wnętrzności całkowicie przebudowane do używania
Lexera, dostarczając wydajność zbliżoną do natywnego rozszerzenia XML,
a także znacząco ulepszoną, modularną architekturę znacznie
ułatwiającą dodawanie nowej funkcjonalności.

Z wersją 3.x związane jest dostrajanie API i zachowania oraz
dostępność mechanizmu do rozróżniania sztuczek HTML-owych ze źle
uformowanych dokumentów (dalsza funkcjonalność nie została jeszcze
zaimplementowana).

Duże podziękowania należą się Jeffowi Moore (głównemu programiście
WACT: http://wact.sourceforge.net/), który jest w znaczący sposób
odpowiedzialny za nowy projekt, a także kod od innych członków forów
http://www.sitepointforums.com/showthread.php?threadid=121246.

Podziękowania należą się także Marcusowi Bakerowi (głównemu
programiście SimpleTestu: http://www.lastcraft.com/simple_test.php) za
uporządkowanie testów jednostkowych.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/XML/*.php
%{php_pear_dir}/XML/HTMLSax3
