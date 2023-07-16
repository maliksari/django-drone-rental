from PIL import Image
from io import BytesIO

class ImageCompressor:
    def compress(self, image):
        compressed_images = {}
        
        try:
            # Orijinal görüntüyü açın
            img = Image.open(image)
            
            # Sıkıştırma işlemini yapın
            compressed_img = self.compress_image(img)
            
            # Sıkıştırılmış görüntüyü belleğe kaydedin
            compressed_image_buffer = BytesIO()
            compressed_img.save(compressed_image_buffer, format='JPEG', quality=90)
            compressed_image_buffer.seek(0)
            
            # Sıkıştırılmış görüntüyü compressed_images sözlüğüne kaydedin
            compressed_images['original'] = compressed_image_buffer
        except Exception as e:
            # Sıkıştırma işlemi başarısız olduysa hata mesajı döndürün
            print(str(e))
        
        return compressed_images
    
    def compress_image(self, img):
        # Görüntüyü istediğiniz şekilde sıkıştırın
        # Örneğin, boyutu 800x800 piksel ile sınırlayabilirsiniz:
        max_size = (800, 800)
        img.thumbnail(max_size, Image.ANTIALIAS)
        
        return img