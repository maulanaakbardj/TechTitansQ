CREATE DATABASE db_pc
CREATE TABLE items(kode_barang INT PRIMARY KEY NOT_NULL, nama_barang VARCHAR(64) NOT_NULL, harga_barang INT NOT_NULL, total_barang INT NOT_NULL)
INSERT INTO items VALUES (1234, "Laptop ASUS X453MA", 4000000, 100)
INSERT INTO items VALUES (1235, "Macbook Air MD2015", 14000000, 20)
INSERT INTO items VALUES (1236, "Printer Epson", 1000000, 40)
INSERT INTO items VALUES (1237, "Flashdisk Kingston 8GB", 80000, 80)
INSERT INTO items VALUES (1238, "Intel Core i5", 2200000, 10)


INSERT INTO items VALUES (1234, "Laptop ASUS X453MA", 4000000, 100)
INSERT INTO items VALUES (1235, "Macbook Air MD2015", 14000000, 20)
INSERT INTO items VALUES (1236, "Printer Epson", 1000000, 40)
INSERT INTO items VALUES (1237, "Flashdisk Kingston 8GB", 80000, 80)
INSERT INTO items VALUES (1238, "Intel Core i5", 2200000, 10)

SELECT * FROM items WHERE kode_barang=1238
UPDATE items SET nama_barang="Intel Core i5 4594" WHERE kode_barang=1238
UPDATE items SET nama_barang="Kingston 8GB" WHERE nama_barang="Flashdisk Kingston 8GB"
SELECT * FROM items WHERE harga_barang>10000000
DELETE FROM items WHERE nama_barang="Printer Epson"
