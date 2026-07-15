import os

from django.conf import settings
from django.core.files import File
from portfolio.models import (
    UnidadeCurricular,
    Tecnologia,
    Projeto,
    Professor,
    Aluno,
    MakingOf
)


def migrar(modelo, campo):
    for obj in modelo.objects.all():

        ficheiro = getattr(obj, campo)

        if ficheiro and ficheiro.name:

            local_path = os.path.join(settings.MEDIA_ROOT, ficheiro.name)
            local_path = local_path.replace("media/media/", "media/")

            if os.path.exists(local_path):

                try:

                    with open(local_path, "rb") as f:

                        ficheiro.save(
                            os.path.basename(local_path),
                            File(f),
                            save=True
                        )

                    print(f"Migrado: {modelo.__name__} -> {obj}")

                except Exception as e:
                    print(f"Erro em {obj}: {e}")

            else:
                print(f"Ficheiro não encontrado: {local_path}")


migrar(UnidadeCurricular, "imagem")
migrar(Tecnologia, "logo")
migrar(Projeto, "imagem")
migrar(Aluno, "foto_perfil")
migrar(MakingOf, "imagem")

print("\nMigração de todos os ficheiros concluída com sucesso!")