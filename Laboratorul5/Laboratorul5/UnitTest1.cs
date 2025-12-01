using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;

namespace Laboratorul5
{
	public class YouTubeSearchTest
	{
		private IWebDriver driver;

		[SetUp]
		public void Setup()
		{
			var options = new ChromeOptions();
			options.AddArgument("--start-maximized");
			driver = new ChromeDriver(options);
		}

		[Test]
		public void SearchComputer_CheckYouTubeHeaderDisplayed()
		{
			// Deschide youtube.com
			driver.Navigate().GoToUrl("https://www.youtube.com");

			// Caută "computer"
			var searchBox = driver.FindElement(By.Name("search_query"));
			searchBox.SendKeys("computer");
			searchBox.Submit();

			// Verifică dacă antetul YouTube (logo) este afișat
			var logo = driver.FindElement(By.Id("logo-icon"));
			Assert.That(logo.Displayed, Is.True, "Antetul YouTube nu este afișat!");
		}

		[TearDown]
		public void TearDown()
		{
			driver?.Quit();
			driver?.Dispose();
		}
	}
}
