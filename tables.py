sql_create_earnings_table = """ CREATE TABLE IF NOT EXISTS earnings (
                                    year INTEGER NOT NULL,
                                    month_name TEXT NOT NULL,
                                    month_number INTEGER NOT NULL,
                                    concept TEXT NOT NULL,
                                    amount REAL NOT NULL,
                                    
                                    PRIMARY KEY(year, month_number, month_name, concept, amount)
                                );"""
