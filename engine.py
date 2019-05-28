from multiprocessing import Process, Manager, Value
import random
import time

sensor_depan        = Value('i', 0)
sensor_belakang     = Value('i', 0)
sensor_depan_kiri   = Value('i', 0)
sensor_depan_kanan  = Value('i', 0)
sensor_kanan        = Value('i', 0)
sensor_kiri         = Value('i', 0)

energy              = Value('i', 30000)
kecepatan           = Value('i', 0)
jarak_tempuh        = Value('i', 0)

pesan_aksi_sensor_jarak = Manager().Value('c', 0)

def sensorDepan():
    sensor_depan.value = random.randint(100, 3000)

def sensorBelakang():
    sensor_belakang.value = random.randint(200, 3000)

def sensorDepanKiri():
    sensor_depan_kiri.value = random.randint(50, 500)

def sensorDepanKanan():
    sensor_depan_kanan.value = random.randint(50, 500)

def sensorKanan():
    sensor_kanan.value = random.randint(50, 500)

def sensorKiri():
    sensor_kiri.value = random.randint(50, 500)

def tambahKecepatan(n):
    if kecepatan.value <= 65:
        kecepatan.value += n

def kurangiKecepatan(n):
    if kecepatan.value >= 0:
        kecepatan.value -= n

def masterKontrol():
    # kontrol kecepatan
    if sensor_depan.value in range(1000, 3000):
        if kecepatan.value > 65:
            kurangiKecepatan(5)
        else:
            tambahKecepatan(7)
    elif sensor_depan.value in range(700, 1000):
        if kecepatan.value > 65:
            kecepatan.value = 45
            kurangiKecepatan(5)
        else:
            tambahKecepatan(4)
    elif sensor_depan.value in range(400, 700):
        if kecepatan.value > 40:
            kecepatan.value = 30
            kurangiKecepatan(5)
        else:
            tambahKecepatan(2)

    elif sensor_depan.value in range(200, 400):
        if kecepatan.value > 40:
            kecepatan.value = 20
            kurangiKecepatan(5)
        else:
            tambahKecepatan(2)

    # kontrol jarak tempuh
    jarak_tempuh.value += int(kecepatan.value/3.6)

    # kontrol energi
    if energy.value > 0:
        energy.value -= int(kecepatan.value/3.6)
    else:
        time.sleep(10)

    # kontrol jarak
    pesan_aksi_sensor_jarak.value = 'Jarak aman'

    if sensor_depan.value in range(0, 200):
        pesan_aksi_sensor_jarak.value = 'Jarak depan terlalu dekat. rem perlahan'
        if kecepatan.value in range(30, 60):
            kurangiKecepatan(20)

    if sensor_kiri.value in range(0, 200):
        pesan_aksi_sensor_jarak.value = 'Geser ke kanan'

    if sensor_kanan.value in range(0, 200):
        pesan_aksi_sensor_jarak.value = 'Geser ke kiri'

    if sensor_depan_kanan.value in range(50, 150):
        pesan_aksi_sensor_jarak.value = 'Geser serong kiri'

    if sensor_depan_kiri.value in range(50, 150):
        pesan_aksi_sensor_jarak.value = 'Geser serong kanan'

def start_engine():
    processSensorDepan      = Process(target=sensorDepan)
    processSensorBelakang   = Process(target=sensorBelakang)
    processSensorDepanKiri  = Process(target=sensorDepanKiri)
    processSensorDepanKanan = Process(target=sensorDepanKanan)
    processSensorKanan      = Process(target=sensorKanan)
    processSensorKiri       = Process(target=sensorKiri)
    processMasterKontrol    = Process(target=masterKontrol)

    processSensorDepan.start()
    processSensorBelakang.start()
    processSensorDepanKiri.start()
    processSensorDepanKanan.start()
    processSensorKiri.start()
    processSensorKanan.start()
    processMasterKontrol.start()

    processSensorDepan.join()
    processSensorBelakang.join()
    processSensorDepanKiri.join()
    processSensorDepanKanan.join()
    processSensorKanan.join()
    processSensorKiri.join()
    processMasterKontrol.join()