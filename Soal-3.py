#!/usr/bin/env python
# coding: utf-8

# In[5]:


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

