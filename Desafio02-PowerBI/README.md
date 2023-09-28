
# DIO-Santander-Bootcamp-2023


# resposta 3 :
    Existe apena um valor nulo na tabela employee e o campo é nulo pois o empregado é um gerente. 

# Resposta 4:      
	O Colaborador James E  Borg - 888665555 está com o valor super_ssn nulo.
## Consulta para validar os dados
	    SELECT * FROM azure_company.employee e
		    where e.Super_ssn is null;

# Resposta 5:
	Não existe departamento sem gerentes.
## Consulta para validar os dados
	    SELECT d.* FROM azure_company.departament d
	    Inner join employee e on e.ssn = d.Mgr_ssn;

# Resposta 6: 
	Não existe departamento sem gerente.

# Resposta 7: 
## Consulta para validar os dados
	    SELECT prj.Pname, sum(wo.Hours), prj.Pname FROM azure_company.works_on wo
	    Inner join azure_company.project prj on prj.Pnumber = wo.Pno Group by prj.Pname ;

# Resposta 8:     
	A Coluna Address da tabela employee é complexa e foram criadas quatro novas colunas;

# Resposta 11: 
## SQL utilizado para resolver a pergunta
    SELECT emp.Ssn, emp.Fname,emp.Lname, emp.Bdate, emp.Super_ssn,Mgr.Fname,Mgr.Lname FROM azure_company.employee emp
    Left join azure_company.employee Mgr ON emp.Super_ssn = Mgr.Ssn;

# Resposta 13: 
    Efetuado o merge entre as colunas 

# Resposta 14: 
    Foi feito o mesclar coluna pois essa atividade substitui as colunas envolvidas por apenas uma com os dados concatenados. 
    Já o atribuir será criada uma nova coluna e as envolvidas no processo vão continuar na tabela.
