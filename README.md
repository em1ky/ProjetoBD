# Estruturação de Banco de Dados

## Ideia do Projeto

Este projeto simula a necessidade de uma imobiliária lidar com as informações do seu site. Considerando essas questões, o projeto realiza a documentação do desenvolvimento da estruturação do banco de dados em diversas etapas.

## Modelo Mer

Como citado anteriormente, realizamos a estruturação de um banco de dados. Uma das etapas iniciais foi a criação de um modelo MER.

![modelo mer](/imagens/imóvelfacil.png)


## Script de Criação 

Após a realização do modelo MER, utilizamos um script gerado pelo próprio programa. Caso esteja interessado, pode encontrar mais informações na documentação do projeto. O resultado é semelhante a este exemplo:

```sql
-- -----------------------------------------------------
-- Schema iziImoveis
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `iziImoveis` DEFAULT CHARACTER SET utf8 ;
USE `iziImoveis` ;

-- -----------------------------------------------------
-- Table `iziImoveis`.`Tb_Secao`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `iziImoveis`.`Tb_Secao` (
  `idTb_Secao` INT NOT NULL,
  `Inicio_de_navegacao` DATETIME NULL,
  `Termino_de_navegacao` DATETIME NULL,
  `Dispositivo` VARCHAR(45) NULL,
  `Qt_paginas_visitadas` INT NULL,
  PRIMARY KEY (`idTb_Secao`))
ENGINE = InnoDB;
...
````
## População dos scripts 

por estamos lidando com uma quantidade massiva de tabelas e informaçoes foi ultilizado programas de terceiros para popuar os scripts que nesse foi usado o site [Mockaroo](https://www.mockaroo.com/)
gerando um resultado similar a esse : 

![Script](/imagens/mockarro.png)

## Power BI

E para realizar a analise das informaçoes necessarios usamos o power bi gerando assim uma [apresentação](https://app.powerbi.com/view?r=eyJrIjoiZmE1NmE4NDEtMWFlYy00MzI0LWFhODAtZThiOGVjMjZlNzZlIiwidCI6ImNmNzJlMmJkLTdhMmItNDc4My1iZGViLTM5ZDU3YjA3Zjc2ZiIsImMiOjR9&embedImagePlaceholder=true) apos a montegem das informaçoes chegamos nesse resultado
![Apresentação](/imagens/imagem.png)
