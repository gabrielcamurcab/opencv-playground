import cv2

# Ler e exibir imagem original
image = cv2.imread("imagem2.jpg")
cv2.imshow("Imagem original", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Converter a imagem em escala de cinza
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Imagem em PB", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Aplicar detector de bordas
edges = cv2.Canny(gray_image, 100, 500)
cv2.imshow("Imagem com bordas detectadas", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()