import pytest
from pages.main_page import MainPage

class TestDemo:

    def test_criar_e_inscrever_aluno(self, driver):
        main_page = MainPage(driver)
        
        # Step: Abrir a página
        driver.get("http://localhost:5000/")

        # cenario: Criar um aluno
        aluno_text = main_page.criar_aluno("alessandro")
        assert "Added student" in aluno_text

        # cenario: Criar três cursos
        curso1_text = main_page.criar_curso("mat")
        curso2_text = main_page.criar_curso("port")
        curso3_text = main_page.criar_curso("geo")
        assert "Added course" in curso1_text
        assert "Added course" in curso2_text
        assert "Added course" in curso3_text

        # cenario: Inscrever o aluno no curso de ID 1
        inscricao_text = main_page.inscrever_aluno_no_curso(student_id="1", course_id="1")
        assert "Added student to course" in inscricao_text

        # cenario: Adicionar três disciplinas ao curso de ID 1
        disciplina1_text = main_page.adicionar_disciplina("mat", "1")
        disciplina2_text = main_page.adicionar_disciplina("mat2", "1")
        disciplina3_text = main_page.adicionar_disciplina("mat3", "1")
        assert "Added discipline" in disciplina1_text
        assert "Added discipline" in disciplina2_text
        assert "Added discipline" in disciplina3_text

        # cenario: Inscrever aluno nas disciplinas de ID 1, 2 e 3
        inscricao_disc1_text = main_page.inscrever_aluno_na_disciplina(student_id="1", discipline_id="1")
        inscricao_disc2_text = main_page.inscrever_aluno_na_disciplina(student_id="1", discipline_id="2")
        inscricao_disc3_text = main_page.inscrever_aluno_na_disciplina(student_id="1", discipline_id="3")
        assert "Enrolled in discipline" in inscricao_disc1_text
        assert "Enrolled in discipline" in inscricao_disc2_text
        assert "Enrolled in discipline" in inscricao_disc3_text