use bancobasico;

create table produtos(
id int auto_increment primary key,
nome varchar(100),
preco decimal(5,2)
);

Create table categorias(
id int auto_increment primary key,
nome varchar(100)
);

insert into produtos(nome, preco)
values ("Banana", 9.50);

select * from produtos;

update produtos
set preco = 8.90
where id = 1;

insert into produtos (nome, preco)
values("Abacaxi", 10.80),
	  ("Melão", 9.20),
      ("Morango", 5.99),
      ("Pera", 4.80);
      
update produtos
set preco = 2.90
where id = 4;

alter table produtos
add column categoria_id int,
add foreign key (categoria_id) references categorias(id);

insert into categorias(nome)
values ("Frutas"),
	   ("Verduras"),
       ("Laticínios");

update produtos 
set categoria_id = 1
where id in (1, 2, 3, 4, 5);

select 
		p.id,
        p.nome as produto,
        p.preco,
        c.nome as categoria
from 
       produtos p
       
join categorias c on p.categoria_id = c.id;

