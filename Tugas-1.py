#!/usr/bin/env python
# coding: utf-8

# In[7]:


Nama=input("Nama saya:")
Umur=input("Umur saya:")
Tinggi=input("Tinggi saya:")
print("Nama saya "+ Nama + ", umur saya " + Umur + " tahun dan tinggi saya " + Tinggi + " cm.")


# In[37]:


r=float(input("jari-jari = "))
phi=float(22/7)
luas_lingkaran= format(phi*r**2, ".2f")
print("Luas lingkaran dengan jari-jari {0} cm adalah {1} cm\u00b2".format(r, luas_lingkaran))


# In[42]:


Ujian_teori=float(input("Nilai Ujian Teori: "))
Ujian_praktek=float(input("Nilai Ujian Praktek: "))
if Ujian_teori >=70 and Ujian_praktek >=70:
    print("Selamat, anda lulus!")
elif Ujian_teori >=70 and Ujian_praktek <70:
    print("Anda harus mengulang ujian praktek.")
elif Ujian_teori <70 and Ujian_praktek >=70:
    print("Anda harus mengulang ujian teori.")
else:
    print("Anda harus mengulang ujian teori dan praktek.")


# In[ ]:




