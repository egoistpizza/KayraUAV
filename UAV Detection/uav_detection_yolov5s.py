# -*- coding: utf-8 -*-
"""UAV_Detection_YOLOv5s

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19_Sx33Mxxmqn6jTmzdwvGPYAtNchN8ad

# KAYRA UAV Team - UAV Detection Systems

![kayra-logo.png](data:image/png;base64,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)

---


## Bu kod nedir?
Bu kod, KAYRA UAV Team'in TEKNOFEST 2023 Savaşan İHA yarışması ve devamındaki projelerinde kullanmak üzere tasarladığı; YOLO v5s nesne tespit algoritmasını ve DeepSORT nesne takip algoritmasını kullanarak (fiziksel) otonom takip yapılmasına olanak tanıyan bir çalışmadır. Aktif olarak geliştirilmeye devam etmektedir.


---


## İletişim
Öneri ve sorularınızı kolaylıkla iletebilmeniz ve çalışmalarımızı takip edebilmeniz için iletişim bilgilerimiz aşağıda yer almaktadır:

Websitesi: [kayraproject.org](https://www.kayraproject.org/)

E-Mail: kayraproject@gmail.com

LinkedIn: [KAYRA UAV Team](https://www.linkedin.com/company/kayra-uav-team/)

Instagram: [@kayrauavproject](https://www.instagram.com/kayrauavproject/)

Twitter: [@KayraUAVTeam](https://twitter.com/KayraUAVTeam)

---


## Lisans
Bu kod ve KAYRA UAV Team - UAV Detection Dataset başta olmak üzere tüm KAYRA PROJECT çalışmaları GNU GPL v3 ile lisanslıdır. [Daha fazla bilgi için tıklayınız](https://www.gnu.org/).

© 2023 KAYRA UAV Team

# 1 - Kurulum

Eğitim ve validation işlemleri için kullanılan datasetin içe aktarılabilmesi için öncelikle google.colab modülünden drive fonksiyonunu içe aktarıyoruz. İstereseniz dataset'i ayrıca indirebilir, inceleyebilir, düzenleyebilir ve direkt olarak kendi sabit diskinizden de işlemlere devam edebilirsiniz.

Ardından nesne tespit işlemi için kullandığımız YOLO v5 algoritmasını Git aracılığıyla klonluyor ve gereksinimlerini pip üzerinden indiriyoruz.

Sonrasında eğitim için gerekli torch modülünü ve bazı fonksiyonlar için ihtiyaç duyduğumuz utils modülünü içe aktararak işlemlerimizi kontrol ediyoruz.
"""

from google.colab import drive
drive.mount("/content/drive")

# Commented out IPython magic to ensure Python compatibility.
!git clone https://github.com/ultralytics/yolov5   # YOLO v5 klonlama
# %cd yolov5
# %pip install -qr requirements.txt   # Gereksinimler indiriliyor

import torch
import utils
display = utils.notebook_init()   # Kontrol ediliyor

!unzip -q /content/drive/MyDrive/dataset.zip -d ../   # .zip olarak sıkıştırılmış dataset'imizi arşivden çıkartıyoruz

"""# 2 - Eğitim ve Analiz

Aktif bir eğitim sürecinin gidişatını veya tamamlanmış bir eğitim sürecinin geçmişini analiz etmek için birçok etkili yöntem bulunmaktadır. Biz bu projemizde [wandb.ai](https://wandb.ai/) kullandık.

Aşağıdaki kod öncelikle wandb'yi pip aracılığıyla indirir. Sonrasında içe aktararak login işlemini başlatır. [Size sunulan adres üzerinden](https://wandb.ai/authorize) tarayıcınızda wandb.ai websitesinde oturum açarak verilecek doğrulama kodunu aşağıya girmeniz istenir. İşlemin tamamlanması durumunda eğitim sürecini hesabınız üzerinden analiz edebilirsiniz.

Ardından eğitim işlemini başlatabilirsiniz. Epoch değeri algoritmanın tekrar sayısıdır; arttırmanız durumunda ağırlıklardan (weights) alacağınız verim artarken kaynak tüketiminiz de artar, azaltmanız durumunda ise tam tersi yaşanır. Data parametresine verdiğimiz .yaml dosyası ise işaretlenecek sınıf bilgilerini içermektedir. yolov5/data dizininde bulunan coco.yaml dosyası iyi bir örnektir, dosyayı düzenleyerek kendi probleminize uygun hale getirebilir ve kullanabilirsiniz. Weights parametresine verdiğimiz yolov5s.pt dosyası YOLO v5s algoritması için öntanımlı değerler bütünüdür, işlemi hızlandırır ve kolaylaştırır.
"""

# Commented out IPython magic to ensure Python compatibility.
# %pip install -q wandb
import wandb
wandb.login()

# YOLO v5s eğitimi
!python train.py --img 640 --batch 16 --epochs 30 --data customset.yaml --weights yolov5s.pt --cache

"""# 3 - Test ve Doğrulama

Eğitim sonucu oluşan modelinizin test ve doğrulama (validation) işlemlerini aşağıdaki kod aracılığıyla yapabilirsiniz. Weights parametresine verdiğimiz dizin önceki başlık altında gerçekleştirdiğimiz eğitim sonucu elde ettiğimiz ağırlıklardır. Önceki kodun çıktısında kaydedildiği dizin bilgisine ulaşabilirsiniz. Data parametresine verdiğimiz değer de yine önceki başlıktaki gibi sınıf değerlerimizi içeren .yaml dosyasıdır.
"""

!python val.py --weights runs/train/exp/weights/best.pt --data customset.yaml --img 640 --half

"""# 4 - Nesne Tespiti

Şimdiyse sıra eğitip doğruladığımız ağırlıkları gerçek zamanlı veya tek seferlik nesne tespiti uygulamalarında kullanmaya geldi. Weights parametresine verdiğimiz değer eğitim sonucu elde ettiğimiz ağırlıklarımız. Source değeri ise nesne tespiti işlemini uygulayacağımız örneği belirtmektedir.
"""

!python detect.py --weights runs/train/exp/weights/best.pt --img 640 --conf 0.25 --source videoplayback.mp4