import sqlite3
cn = sqlite3.connect('factbook.db')
cs = cn.cursor()
it = cs.execute('select avg(population), avg(population_growth), avg(birth_rate), avg(death_rate) from facts;').fetchall()
cn.close()

pop_avg = it[0][0]
pop_growth_avg = it[0][1]
birth_rate_avg = it[0][2]
death_rate_avg = it[0][3]

averages = "select avg(population), avg(population_growth), avg(birth_rate), avg(death_rate), avg(migration_rate) from facts;"
avg_results = conn.execute(averages).fetchall()
pop_avg = avg_results[0][0]
pop_growth_avg = avg_results[0][1]
birth_rate_avg = avg_results[0][2]
death_rate_avg = avg_results[0][3]
mig_rate_avg = avg_results[0][4]

minmax = "select min(population), max(population), min(population_growth), max(population_growth), min(birth_rate), max(birth_rate), min(death_rate), max(death_rate) from facts;"
minmax_results = conn.execute(minmax).fetchall()
print (minmax_results)
pop_min = minmax_results[0][0]
pop_max = minmax_results[0][1]
pop_growth_min = minmax_results[0][2]
pop_growth_max = minmax_results[0][3]
birth_rate_min = minmax_results[0][4]
birth_rate_max = minmax_results[0][5]
death_rate_min = minmax_results[0][6]
death_rate_max = minmax_results[0][7]

cs = cn.cursor()
it = cs.execute('select min(population), max(population), min(population_growth), max(population_growth), min(birth_rate), max(birth_rate), min(death_rate), max(death_rate) from facts where population<2000000000 and population>0;').fetchall()
cn.close()

pop_min = it[0][0]
pop_max= it[0][1]
pop_growth_min= it[0][2]
pop_growth_max= it[0][3]
birth_rate_min= it[0][4]
birth_rate_max= it[0][5]
death_rate_min= it[0][6]
death_rate_max= it[0][7]

cs = cn.cursor()
projected_population = cs.execute('select round(population*(1+population_growth/100)) from facts where population!="NULL" and population_growth!="NULL" and population>0 and population<7000000000;').fetchall()
cn.close()

proj_pop_query = '''
select round(min(population + population * (population_growth/100)), 0), 
round(max(population + population * (population_growth/100)), 0), 
round(avg(population + population * (population_growth/100)), 0)
from facts 
where population > 0 and population < 7000000000 and 
population is not null and population_growth is not null;
'''

proj_results = conn.execute(proj_pop_query).fetchall()

pop_proj_min = proj_results[0][0]
pop_proj_max = proj_results[0][1]
pop_proj_avg = proj_results[0][2]

print("Projected Population,", "Minimum: ", pop_proj_min)
print("Projected Population,", "Maximum: ", pop_proj_max)
print("Projected Population,", "Average: ", pop_proj_avg)

