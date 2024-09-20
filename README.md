***ServoGlobalTunnel-http***

This Python script allows you to expose your local web server to the global internet using Serveo.net. It sets up a reverse SSH tunnel from your local machine to Serveo, making your localhost accessible from anywhere in the world.


**Requirements:**

Python 3.x,
SSH client installed on your system,
Linux and macOS come with SSH pre-installed,
Windows users may need to install SSH manually or enable it from Optional Features.

**Usage:**

Ensure your local server is running on port 80.

Make sure that port 80 is open and not blocked by any firewall on your machine.

Run the Python script with the following command:

python servo_global_tunnel_http.py

The script will establish a reverse SSH tunnel through Serveo and provide a globally accessible URL to your localhost.

**Notes:**

On Windows, make sure that the SSH client is installed. You can enable it through "Manage Optional Features" or use an external tool like PuTTY.
For the tunnel to work correctly, ensure port 80 is open on your local machine.

*********************************************************************************************************************************************************************************************************

***ServoGlobalTunnel-http (Türkçe)***

Bu Python betiği, Serveo.net kullanarak yerel web sunucunuzu küresel internete açmanıza olanak tanır. Betik, yerel makinenizden Serveo'ya bir ters SSH tüneli kurarak, localhost'unuzu dünyaya açar.

**Gereksinimler:**

Python 3.x,
SSH istemcisi kurulu olmalıdır,
Linux ve macOS'ta SSH öntanımlı olarak bulunur,
Windows kullanıcıları SSH'yi manuel olarak kurmalı veya Opsiyonel Özellikler'den etkinleştirmelidir.

**Kullanım:**

Yerel sunucunuzun 80. portta çalıştığından emin olun.

Makinenizde 80. portun açık ve herhangi bir güvenlik duvarı tarafından engellenmediğinden emin olun.

Python betiğini şu komutla çalıştırın:

python servo_global_tunnel_http.py

Betik, Serveo aracılığıyla bir SSH tüneli kuracak ve localhost'unuza küresel bir erişim URL'si sağlayacaktır.

**Notlar:**

Windows'ta, SSH istemcisinin yüklü olduğundan emin olun. "Opsiyonel Özellikler" üzerinden etkinleştirebilir veya PuTTY gibi bir araç kullanabilirsiniz.
Tünelin düzgün çalışabilmesi için makinenizde 80. portun açık olması gerekmektedir.
