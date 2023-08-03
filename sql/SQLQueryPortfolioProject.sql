SELECT *
FROM PortfolioProject..CovidDeaths
WHERE continent is not null
ORDER BY 3, 4


--SELECT *
--FROM PortfolioProject..CovidVaccinations
--WHERE continent is not null
--ORDER BY 3, 4


-- Select Data that to use


SELECT Location, date, total_cases, new_cases, total_deaths, population
FROM PortfolioProject..CovidDeaths
WHERE continent is not null
ORDER BY 1,2

-- Looking at total cases vs total deaths
-- Shows likelihood of dying if you contract covid in your country
-- Cast is used to show data as Decimal and DeathPercentage covers the 

SELECT Location, date, total_cases, new_cases, total_deaths, (CAST(total_deaths AS decimal(12,2)) / CAST(total_cases AS decimal(12,2)))*100 AS DeathPercentage
FROM PortfolioProject..CovidDeaths
WHERE LOCATION like '%BRAZIL%' AND continent is not null
ORDER BY 1,2


-- Looking at Total Cases vs Population
-- Shows percentage of population that got covid
SELECT Location, date, total_cases, population, new_cases, (CAST(total_cases AS decimal(12,2)) / CAST(population AS decimal(12,2)))*100 AS PopulationInfectedPercentage
FROM PortfolioProject..CovidDeaths
WHERE LOCATION like '%states%' AND continent is not null
ORDER BY 1,2

-- Looking at countries for Countries with the highest infection rates
SELECT location, population, MAX(total_cases) AS HighestInfectionCount, MAX(CAST(total_cases AS decimal(12,2)) / CAST(population AS decimal(12,2)))*100 AS PercentPopulationInfected
FROM PortfolioProject..CovidDeaths
GROUP BY location, population
ORDER BY PercentPopulationInfected DESC


-- Showing countries with Highest Death count per Population
-- Breaking things down by continent
SELECT location, population, MAX(cast(total_deaths as decimal(12,2))) AS TotalDeathCount
FROM PortfolioProject..CovidDeaths
WHERE continent is not null
GROUP BY location, population
ORDER BY TotalDeathCount DESC

-- Show continent with the highest death count
SELECT continent, MAX(cast(total_deaths as decimal(12,2))) AS TotalDeathCount
FROM PortfolioProject..CovidDeaths
WHERE continent is not null
GROUP BY continent
ORDER BY TotalDeathCount DESC

SELECT location, MAX(cast(total_deaths as decimal(12,2))) AS TotalDeathCount
FROM PortfolioProject..CovidDeaths
WHERE continent is null
GROUP BY location
ORDER BY TotalDeathCount DESC

-- Troubleshooot the divided by zero issue
SET ARITHABORT OFF;
SET ANSI_WARNINGS OFF;

-- Global Numbers, for each passing day
SELECT date, SUM(cast(new_cases AS DECIMAL(12,2))) as TotalCases
,SUM(CAST(new_deaths as DECIMAL(12,2))) as TotalDeaths
,SUM(CAST(new_deaths as DECIMAL(12,2))) / SUM(cast(new_cases as float)) * 100 as Death
FROM PortfolioProject..CovidDeaths
WHERE continent is not null
Group by date
ORDER BY 1,2

-- Global numbers by the final date (2029-07-09)
SELECT SUM(cast(new_cases AS DECIMAL(12,2))) as TotalCases
,SUM(CAST(new_deaths as DECIMAL(12,2))) as TotalDeaths
,SUM(CAST(new_deaths as DECIMAL(12,2))) / SUM(cast(new_cases as float)) * 100 as Death
FROM PortfolioProject..CovidDeaths
WHERE continent is not null
ORDER BY 1,2


-- Looking at total population vs Vaccination

SELECT dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, SUM(CONVERT(float, vac.new_vaccinations)) OVER (Partition by dea.Location ORDER BY dea.location, dea.date) AS RollingPeopleVaccinated
FROM PortfolioProject..CovidDeaths dea
JOIN PortfolioProject..CovidVaccinations vac
	ON dea.location = vac.location
	AND dea.date = vac.date
WHERE dea.continent is not null
ORDER BY 2,3


--Using a CTE, check the percentage of the people who are vaccinated

WITH PopVsVac(continent, Location, Date, Population, new_vaccinations, RollingPeopleVaccinated)
AS
(
SELECT dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, SUM(CAST(vac.new_vaccinations AS DECIMAL(12,2))) OVER (Partition by dea.Location ORDER BY dea.location, dea.date) AS RollingPeopleVaccinated
FROM PortfolioProject..CovidDeaths dea
JOIN PortfolioProject..CovidVaccinations vac
	ON dea.location = vac.location
	AND dea.date = vac.date
WHERE dea.continent is not null
)
SELECT *, (RollingPeopleVaccinated/Population)*100 as PercentageVaccinated
FROM PopVsVac

-- Same as above but using a Temp Table

DROP TABLE IF EXISTS #PercentPopulationVaccinated
CREATE TABLE #PercentPopulationVaccinated
(
Continent nvarchar(255),
Location nvarchar(255),
Date datetime,
Population numeric,
new_vaccionations numeric,
RollingPeopleVaccinated numeric
)


INSERT INTO #PercentPopulationVaccinated
SELECT dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, SUM(CAST(vac.new_vaccinations AS DECIMAL(12,2))) OVER (Partition by dea.Location ORDER BY dea.location, dea.date) AS RollingPeopleVaccinated
FROM PortfolioProject..CovidDeaths dea
JOIN PortfolioProject..CovidVaccinations vac
	ON dea.location = vac.location
	AND dea.date = vac.date
WHERE dea.continent is not null

SELECT *
FROM #PercentPopulationVaccinated

-- Creating view to store data for later visualizations

CREATE VIEW PercentPopulationVaccinated AS
SELECT dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, SUM(CAST(vac.new_vaccinations AS DECIMAL(12,2))) OVER (Partition by dea.Location ORDER BY dea.location, dea.date) AS RollingPeopleVaccinated
FROM PortfolioProject..CovidDeaths dea
JOIN PortfolioProject..CovidVaccinations vac
	ON dea.location = vac.location
	AND dea.date = vac.date
WHERE dea.continent is not null
