-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le :  mer. 18 déc. 2019 à 21:14
-- Version du serveur :  5.7.26
-- Version de PHP :  7.2.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `oc_projet_5_off`
--
-- --------------------------------------------------------

--
-- Structure de la table `category`
--

DROP TABLE IF EXISTS `category`;
CREATE TABLE IF NOT EXISTS `category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) CHARACTER SET utf8mb4 NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf32;

-- --------------------------------------------------------

--
-- Structure de la table `product`
--

DROP TABLE IF EXISTS `product`;
CREATE TABLE IF NOT EXISTS `product` (
  `id` int(5) NOT NULL,
  `name` varchar(150) CHARACTER SET utf8mb4 NOT NULL,
  `nutriscore` char(1) CHARACTER SET utf8mb4 NOT NULL,
  `url` text CHARACTER SET utf8mb4 NOT NULL,
  `store` varchar(150) CHARACTER SET utf8mb4 DEFAULT NULL,
  `category_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_category_id` (`category_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf32;

-- --------------------------------------------------------

--
-- Structure de la table `substitut_product`
--

DROP TABLE IF EXISTS `substitut_product`;
CREATE TABLE IF NOT EXISTS `substitut_product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sub_from` int(5) NOT NULL,
  `sub_to` int(5) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_sub_to` (`sub_to`),
  KEY `fk_sub_from` (`sub_from`)
) ENGINE=InnoDB DEFAULT CHARSET=utf32;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `product`
--
ALTER TABLE `product`
  ADD CONSTRAINT `cat_product` FOREIGN KEY (`category_id`) REFERENCES `category` (`id`);

--
-- Contraintes pour la table `substitut_product`
--
ALTER TABLE `substitut_product`
  ADD CONSTRAINT `fk_sub_from` FOREIGN KEY (`sub_from`) REFERENCES `product` (`id`),
  ADD CONSTRAINT `fk_sub_to` FOREIGN KEY (`sub_to`) REFERENCES `product` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
