library("ggplot2")
library("openxlsx")

#Membaca file mahasiswa.xlsx
mahasiswa <- read.xlsx("https://academy.dqlab.id/dataset/mahasiswa.xlsx",
                       sheet = "Sheet 1")

#Menghitung Jumlah Data by Fakultas
summarybyfakultas <- aggregate(x=mahasiswa$JUMLAH,
                               by=list(Kategori=mahasiswa$Fakultas,
                                       Tahun=mahasiswa$ANGKATAN), 
                               FUN=sum)

summarybyfakultas <- setNames(summarybyfakultas,
                              c("fakultas","tahun", "jumlah_mahasiswa"))

summarybyfakultas$tahun = as.factor(summarybyfakultas$tahun)

ggplot(summarybyfakultas[summarybyfakultas$fakultas %in% 
                           c("ICT", "Ilmu Komunikasi"),], 
       aes(x=fakultas, y=jumlah_mahasiswa)) + 
  geom_bar(stat = "identity", 
           aes(fill = tahun), 
           width=0.8, 
           position = position_dodge(width=0.8)) + 
  theme_classic()
