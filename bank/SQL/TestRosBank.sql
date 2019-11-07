USE [TestTable]
GO

/****** Object:  Table [dbo].[TableRosBank]    Script Date: 01.11.2019 16:08:04 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[TableRosBank](
	BankID int IDENTITY(1,1),
	[Month] [date] NULL,
	[TO] [nvarchar](50) NOT NULL,
	[City] [nvarchar](50) NOT NULL,
	[Office] [decimal](18, 0) NULL,
	[Financial indicator] [nvarchar](50) NULL,
	[Indicator] [nchar](10) NULL,
	[Value] [int] NULL
) ON [PRIMARY]
GO


ALTER TABLE TableRosBank
ADD BankID int IDENTITY(1,1)
GO

ALTER TABLE TableRosBank
ADD CONSTRAINT PK_TableRosBank_BankID PRIMARY KEY CLUSTERED (BankID)
GO


INSERT INTO TableRosBank (City, Office, [Financial indicator], Indicator) VALUES 
('[Святой Петр]', '1337', 'Финансовые', 'Карты')
GO