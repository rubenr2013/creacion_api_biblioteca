from rest_framework import serializers
from .models import Autor, Libro, Prestamo

class AutorSerializer(serializers.ModelSerializer):
    libros_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Autor
        fields = ['id', 'noombre', 'apellido', 'fecha_nacimiento', 'nacionalidad', 'libros_count']
        
    def get_libros_count(self, obj):
        return obj.libros.count()

class LibroSerializer(serializers.ModelSerializer):
    autor_nombre = serializers.CharField(source='autor.noombre', read_only=True)
    autor_apellido = serializers.CharField(source='autor.apellido', read_only=True)
    
    class Meta:
        model = Libro
        fields = ['id', 'titulo', 'autor', 'autor_nombre', 'autor_apellido', 'isbn', 'fecha_publicacion', 'genero', 'paginas', 'disponible']
        
    def validate_isbn(self, value):
        if len(value) != 13:
            raise serializers.ValidationError("El ISBN debe tener 13 dígitos numéricos.")
        return value

class PrestamoSerializer(serializers.ModelSerializer):  
    libro_titulo = serializers.CharField(source='libro.titulo', read_only=True)
    usuario_nombre = serializers.CharField(source='usuario.username', read_only=True)
    
    class Meta:
        model = Prestamo
        fields = ['id', 'libro', 'libro_titulo', 'usuario', 'usuario_nombre', 'fecha_prestamo', 'fecha_devolucion', 'devuelto']
        
    def create(self, validated_data):  
        libro = validated_data['libro']
        if not libro.disponible:
            raise serializers.ValidationError("El libro no está disponible para préstamo.")
        
        libro.disponible = False
        libro.save()
        return super().create(validated_data)