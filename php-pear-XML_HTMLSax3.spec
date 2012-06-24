%include	/usr/lib/rpm/macros.php
%define		_class		XML
%define		_subclass	HTMLSax3
%define		_status		beta
%define		_pearname	XML_HTMLSax3

Summary:	%{_pearname} - A SAX parser for HTML and other badly formed XML documents
Summary(pl):	%{_pearname} - parser SAX dla HTML-a i innych �le uformowanych dokument�w XML
Name:		php-pear-%{_pearname}
Version:	3.0.0
%define	_rc	RC1
Release:	0.%{_rc}.1
Epoch:		0
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{_rc}.tgz
# Source0-md5:	37032d3e3bb22b66756b686028106a5e
URL:		http://pear.php.net/package/XML_HTMLSax3
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:4.0.5
Requires:	php-pcre
Requires:	php-pear
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

%description -l pl
XML_HTMLSax3 to oparty na SAX parser XML-a dla �le uformowanych
dokument�w XML, takich jak HTML. Oryginalny kod bazowy zosta�
stworzony przez Alexandra Zhukova i opublikowany pod
http://sourceforge.net/projects/phpshelve/. Alexander udzieli�
pozwolenia na modyfikowanie tego kodu oraz licencji na do��czenie do
PEAR-a.

PEAR::XML_HTMLSax3 udost�pnia API bardzo podobne do natywnego
rozszerzenia PHP XML (http://www.php.net/xml), co pozwala na �atwe
dostosowanie procedur obs�uguj�cych u�ywaj�cych jednego API do
drugiego. G��wna r�nica polega na tym, �e HTMLSax nie za�amie si� na
�le uformowanym XML-u, co pozwala na u�ywanie go do przetwarzania
dokument�w HTML. Poza tym HTMLSax obs�uguje wszystkie procedury
obs�ugi dost�pne w Expacie z wyj�tkiem procedur obs�ugi przestrzeni
nazw i zewn�trznych encji. Dost�pne s� metody do obs�ugi sekwencji
specjalnych XML, a tak�e znacznik�w otwieraj�cych i zamykaj�cych
JSP/ASP.

Wersja 1.x wprowadzi�a API podobne do natywnego rozszerzenia SAX, ale
u�ywa�a wolnego podej�cia do przetwarzania (znak po znaku).

Wersja 2.x mia�a wn�trzno�ci ca�kowicie przebudowane do u�ywania
Lexera, dostarczaj�c wydajno�� zbli�on� do natywnego rozszerzenia XML,
a tak�e znacz�co ulepszon�, modularn� architektur� znacznie
u�atwiaj�c� dodawanie nowej funkcjonalno�ci.

Z wersj� 3.x zwi�zane jest dostrajanie API i zachowania oraz
dost�pno�� mechanizmu do rozr�niania sztuczek HTML-owych ze �le
uformowanych dokument�w (dalsza funkcjonalno�� nie zosta�a jeszcze
zaimplementowana).

Du�e podzi�kowania nale�� si� Jeffowi Moore (g��wnemu programi�cie
WACT: http://wact.sourceforge.net/), kt�ry jest w znacz�cy spos�b
odpowiedzialny za nowy projekt, a tak�e kod od innych cz�onk�w for�w
http://www.sitepointforums.com/showthread.php?threadid=121246.

Podzi�kowania nale�� si� tak�e Marcusowi Bakerowi (g��wnemu
programi�cie SimpleTestu: http://www.lastcraft.com/simple_test.php) za
uporz�dkowanie test�w jednostkowych.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

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
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/%{_pearname}
