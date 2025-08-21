// Datos de ejemplo
let empleados_top_10 = []
let promedio_dept = []
let promedio_salario = []
empleados_top.forEach(e => empleados_top_10.push(e.full_name))

avg_department.forEach(d => {promedio_dept.push(d.departamento)})
avg_salario.forEach(d => promedio_salario.push(d.salario))


const ctxPastel = document.getElementById('graficoPastel').getContext('2d');
const graficoPastel = new Chart(ctxPastel, {
    type: 'pie',
    data: {
        labels: ["Hombres","Mujeres"],
        datasets: [{
            label: 'Total',
            data: [num_male_employee ,num_female_employee],
            backgroundColor: [
                '#AF3E3E',
                '#FFB4B4'

            ]
        }]
    },
    options: {
        responsive: false,             // se adapta al contenedor
        maintainAspectRatio: true    // permite cambiar ancho/alto
    }
});

const ctxBarrasHorizontal = document.getElementById('graficoBarrasHorizontal').getContext('2d');
const graficoBarrasHorizontal = new Chart(ctxBarrasHorizontal, {
    type: 'bar',   // vertical por defecto
    data: {
        labels: empleados_top_10,
        datasets: [{
            label: 'Total',
            data: salarios_top,
            backgroundColor: [
                '#2F4B33',
                '#4B7A55',
                '#6FA77B',
                '#92C49C',
                '#B5E2B7',
                '#D8F2D3',
                '#A0CFA1',
                '#7FB984',
                '#53915F',
                '#346B3C'
            ]
        }]
    },
    options: {
        responsive: false,             // se adapta al contenedor
        maintainAspectRatio: true,
        indexAxis: 'y',  // x = vertical
    }
});

// 3️⃣ Gráfico de barras horizontal
const ctxBarrasVertical = document.getElementById('graficoBarrasVertical').getContext('2d');
const graficoBarrasVertical = new Chart(ctxBarrasVertical, {
    type: 'bar',
    data: {
        labels: promedio_dept,
        datasets: [{
            label: 'Mi gráfico de barras horizontal',
            data: promedio_salario,
            backgroundColor: [
                '#1A2A80',
                '#3B38A0',
                '#7A85C1',
                '#B2B0E8'
            ]
        }]
    },
    options: {
        responsive: false,             // se adapta al contenedor
        maintainAspectRatio: true,
        indexAxis: 'x', // y = horizontal
    }
});
