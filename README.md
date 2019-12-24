Web aplikasyonlarında Front Controller tasarım deseni ile sisteme yöneltilen tüm istekler (request) merkezi bir yerde toplanarak işlem görürler. Front Controller ile yönlendirme ve işlem yapma fonksiyonlarının birden fazla viewlara dağıtılması önlenmiş olur. Tüm viewlar isteğin doğrulanması / yetkilendirilmesi / kaydedilmesi veya izlenmesi fonksiyonlarını ortak kullanırlar. Böylece Front Controller tasarım şablonunun kullanıldığı bir proje bakımı ve geliştirilmesi daha kolay bir hale gelir. 
• Front Controller – Uygulamaya gelen her türlü istek için tek bir yönetici. (web tabanlı / masaüstü tabanlı). 
• Dağıtıcı - Front Controller, talebi ilgili ilgili işleyiciye gönderebilecek bir dağıtıcı nesnesi. 
• View – Viewlar , isteklerin yapıldığı yerdir. 
 
 
 
AVANTAJLARI: • Merkezi kontrol:– Front Controller , web uygulamasına yapılan tüm istekleri yerine getirir. Birden fazla denetleyicinin kullanılmasını önleyen bu merkezi kontrol uygulaması, kullanıcıları izlemesi ve güvenliği için uygundur. 
• İş parçacığı güvenliği(Thread-safety):- Her şey tek bir yerden olduğu için thread safe bir design patterndir. Command classları içinde thread safety vardır. 
 
 
 
DEZAVANTAJLARI: • Ön denetleyici kullanarak bir uygulamayı geliştirmek mümkün değildir. 
 
• Tek bir istekle ilgilendiği zaman performansı artar. 
