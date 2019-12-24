################ Front Controller Pattern

Web aplikasyonlarında Front Controller tasarım deseni ile sisteme yöneltilen tüm istekler (request) merkezi bir yerde toplanarak işlem görürler. Front Controller ile yönlendirme ve işlem yapma fonksiyonlarının birden fazla viewlara dağıtılması önlenmiş olur. Tüm viewlar isteğin doğrulanması / yetkilendirilmesi / kaydedilmesi veya izlenmesi fonksiyonlarını ortak kullanırlar. Böylece Front Controller tasarım şablonunun kullanıldığı bir proje bakımı ve geliştirilmesi daha kolay bir hale gelir. 
• Front Controller – Uygulamaya gelen her türlü istek için tek bir yönetici. (web tabanlı / masaüstü tabanlı). 
• Dağıtıcı - Front Controller, talebi ilgili ilgili işleyiciye gönderebilecek bir dağıtıcı nesnesi. 
• View – Viewlar , isteklerin yapıldığı yerdir. 
 
 
 
AVANTAJLARI: 
• Merkezi kontrol:– Front Controller , web uygulamasına yapılan tüm istekleri yerine getirir. Birden fazla denetleyicinin kullanılmasını önleyen bu merkezi kontrol uygulaması, kullanıcıları izlemesi ve güvenliği için uygundur. 
• İş parçacığı güvenliği(Thread-safety):- Her şey tek bir yerden olduğu için thread safe bir design patterndir. Command classları içinde thread safety vardır. 
 
DEZAVANTAJLARI: 
• Ön denetleyici kullanarak bir uygulamayı geliştirmek mümkün değildir.  
• Tek bir istekle ilgilendiği zaman performansı artar. 

################ Visitor Pattern

Visitor tasarım deseni (ziyaretçi tasarım deseni), behavioral grubuna ait inceleyeceğimiz son tasarım desenidir. Uygulamada ki sınıflara yeni metotlar eklenmesini düzenleyen bir tasarım desenidir. Dofactory.com a göre kullanım sıklığı 20% civarındadır.
Uygulamada ki bir yapıda ki bazı sınıflara bir işlevsellik eklenmesi gerektiğinde genelde ya yapıdaki sınıfların uyguladığı arayüzde metot tanımlanır ve bu arayüzü uygulayan sınıflarda metot yazılır veya eklenmesi gereken sınıflara eklenir. Arayüze metot tanımlarsak metodu kullanmayacak olan sınıflarda da bu metot uygulanacağı için tasarım prensiplerinden “Interface Segregation Principle - ISP” a uymamış oluruz. İlgili alt sınıflara ayrı ayrı metot eklersek de ileride bakımı zorlaşacak ve kodun karışmasına neden olacak bir yapı kurmuş oluruz. Böyle durumlarda bu hatalara düşmemek için visitor tasarım deseni kullanılabilir. 

Visitor, ConcreteElement sınıflarının yani Element arayüzünü uygulayan sınıfların kullanabileceği metotların tanımlandığı arayüzdür. Şöyle ki burada tanımlanan metotlar parametre olarak ConcreteElement sınılarını alırlar ve bu sınıflar üzerinden işlem yapabilirler. Bu da Element arayüzündeki Accept metodu ile yapılır. Bu metot içinde kendisine gönderilen Visitor arayüzünden türeyen nesnede ki Visit metoduna parametre olarak kendisini vererek yapar. Böylece gönderilen ConcreteVisitor nesnesinde ki ilgili Visit metodu çalıştırılmış olunur.


