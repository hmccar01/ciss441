import sqlite3
dbfile = 'payroll_dc_small.db' #This is the database file
conn = sqlite3.connect(dbfile) #This is being used to connect the databasse
print("The database has been opened")

row_format_string = "{0:<25} {1:<15} {2:<10} {3:10}"
print(row_format_string.format("Education Level", "Type", "salmax", "salmin"))

cursor = conn.execute(
		"""
		select edlvl.edlvltypt, edlvl.edlvlt, max(f.salary) salmax,min(f.salary) salmin
		from factdata_mar2016 f, edlvl
		where f.edlvl=edlvl.edlvl
		group by edlvl.edlvltypt, edlvl.edlvlt
		order by salmax desc
		limit 20;
		""")
		
for row in cursor:
	Education_level, Type, salmax, salmin = row
	print(row_format_string.format(Education_level, Type[0:14], salmax, salmin))
	
print("\nThis report shows the maximum and minimum salaries.")
conn.close
