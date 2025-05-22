-- phpMyAdmin SQL Dump
-- version 5.2.2
-- https://www.phpmyadmin.net/
--
-- Хост: localhost
-- Время создания: Май 22 2025 г., 06:27
-- Версия сервера: 11.7.2-MariaDB
-- Версия PHP: 8.4.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `demo_ekz`
--

-- --------------------------------------------------------

--
-- Структура таблицы `partners`
--

CREATE TABLE `partners` (
  `id` int(11) NOT NULL,
  `title` varchar(200) NOT NULL,
  `type` varchar(50) NOT NULL,
  `headmaster` varchar(150) NOT NULL,
  `mail` varchar(150) NOT NULL,
  `phone` varchar(30) NOT NULL,
  `address` varchar(200) NOT NULL,
  `INN` varchar(20) NOT NULL,
  `rating` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_general_ci;

--
-- Дамп данных таблицы `partners`
--

INSERT INTO `partners` (`id`, `title`, `type`, `headmaster`, `mail`, `phone`, `address`, `INN`, `rating`) VALUES
(1, 'ЗАО', 'База Строитель', 'Иванова Александра Ивановна', 'aleksandraivanova@ml.ru', '493 123 45 67', '652050, Кемеровская область, город Юрга, ул. Лесная, 15', '2222455179', 7),
(2, 'ООО', 'Паркет 29', 'Петров Василий Петрович', 'vppetrov@vl.ru', '987 123 56 78', '164500, Архангельская область, город Северодвинск, ул. Строителей, 18', '3333888520', 7),
(3, 'ПАО', 'Стройсервис', 'Соловьев Андрей Николаевич', 'ansolovev@st.ru', '812 223 32 00', '188910, Ленинградская область, город Приморск, ул. Парковая, 21', '4440391035', 7),
(4, 'ОАО', 'Ремонт и отделка', 'Воробьева Екатерина Валерьевна', 'ekaterina.vorobeva@ml.ru', '444 222 33 11', '143960, Московская область, город Реутов, ул. Свободы, 51', '1111520857', 5),
(5, 'ЗАО', 'МонтажПро', 'Степанов Степан Сергеевич', 'stepanov@stepan.ru', '912 888 33 33', '309500, Белгородская область, город Старый Оскол, ул. Рабочая, 122', '5552431140', 10),
(17, 'a', 'b', 'c', 'd', 'e', 'g', 'f', 1),
(18, 'a', 'b', 'c', 'd', 'e', 'g', 'f', 100),
(19, 'Партер', 'ООО', 'Я', 'почта', 'тел', 'инна', 'ул', 100500),
(20, 'fvhgbj', 'gcfvhbj', 'gfvh', 'gfvhb', 'gfvgb', 'vb ', 'gv b', 2);

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `partners`
--
ALTER TABLE `partners`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `partners`
--
ALTER TABLE `partners`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
