// Zinkro JS: Funciones compartidas para todas las vistas

// Era Holocena: año gregoriano + 10000
function gregorianToHolocene(year) {
  return year + 10000;
}
function holoceneToGregorian(yearHE) {
  return yearHE - 10000;
}
// Formato de fecha HE
function formatHolocene(year, month, day) {
  return `${gregorianToHolocene(year)} HE-${String(month).padStart(2,'0')}-${String(day).padStart(2,'0')}`;
}
// Conversión gregoriano a Zinkro (consistente con Python)
function gregorianToZinkro(dateStr) {
  // dateStr: "YYYY-MM-DD"
  const [year, month, day] = dateStr.split('-').map(Number);
  // Inicio: -10000-03-21
  // Calcular días desde -10000-03-21 hasta la fecha dada
  // Usar algoritmo manual igual al de SimpleDate en Python
  const startYear = -10000;
  const startMonth = 3;
  const startDay = 21;
  function isLeap(year) {
    return (year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0);
  }
  function daysSinceEpoch(y, m, d) {
    let days = y * 365 + (m - 1) * 30 + (d - 1);
    const month_days = [31,28,31,30,31,30,31,31,30,31,30,31];
    if (m > 1) {
      days += month_days.slice(0, m-1).reduce((a,b)=>a+b,0) - (30 * (m-1));
    }
    return days;
  }
  const daysStart = daysSinceEpoch(startYear, startMonth, startDay);
  const daysInput = daysSinceEpoch(year, month, day);
  const delta = daysInput - daysStart;
  // Día Zero: si delta === 0
  if (delta === 0) return { year: 0, diaZero: true };
  // El primer día del año Zinkro es el 22 de marzo, así que el conteo debe iniciar en 1 para ese día
  let yearZ = Math.floor((delta - 1) / 365);
  let dayOfYear = (delta - 1) % 365;
  // Ajuste: el primer día del año Zinkro debe ser el 22 de marzo (no el 21)
  // Si la fecha es el 21 de marzo, es Día Zero
  // Si la fecha es el 22 de marzo, es el día 1 del año Zinkro
  // Si el año gregoriano es bisiesto y la fecha es 29 de febrero, corresponde al día 9 del mes 13
  if (isLeap(year) && month === 2 && day === 29) {
    return { year: yearZ, month: 13, day: 9, diaZero: false, bisiesto: true };
  }
  // En años bisiestos, del 1 al 19 de marzo, los días se recorren uno más en el mes 13
  if (isLeap(year) && month === 3 && day >= 1 && day <= 19) {
    return { year: yearZ, month: 13, day: day + 9, diaZero: false, bisiesto: true };
  }
  // 20 de marzo en año bisiesto: Día 366
  if (isLeap(year) && month === 3 && day === 20) {
    return { year: yearZ, dia366: true, diaZero: false };
  }
  // Día Zero: si delta === 0
  if (delta === 0) return { year: 0, diaZero: true };
  const daysInMonth = 28;
  const monthsInYear = 13;
  // Día extra Zinkro (Día 366)
  if (dayOfYear === daysInMonth * monthsInYear) return { year: yearZ, dia366: true, diaZero: false };
  const monthZ = Math.floor(dayOfYear / daysInMonth) + 1;
  const dayZ = (dayOfYear % daysInMonth) + 1;
  return { year: yearZ, month: monthZ, day: dayZ, diaZero: false };
}
// Conversión Zinkro a gregoriano
function zinkroToGregorian(yearZ, monthZ, dayZ) {
  // Inicio: -10000-03-21
  const start = new Date(-10000, 2, 21);
  let days = yearZ * 365;
  if (monthZ === undefined && dayZ === undefined) {
    // Día 366 Zinkro: corresponde al 29 de febrero gregoriano
    let gregYear = yearZ - 10000;
    while (!((gregYear % 4 === 0 && gregYear % 100 !== 0) || (gregYear % 400 === 0))) {
      gregYear++;
    }
    return new Date(gregYear, 1, 29); // 29 de febrero
  } else if (monthZ) {
    days += (monthZ-1)*28 + (dayZ-1);
  } else {
    days += 364;
  }
  // Sumar días bisiestos desde -10000 hasta el año correspondiente
  let leapDays = 0;
  for (let yr = -10000; yr < yearZ; yr++) {
    if ((yr % 4 === 0 && yr % 100 !== 0) || (yr % 400 === 0)) leapDays++;
  }
  days += leapDays;
  const result = new Date(start.getTime() + days*24*60*60*1000);
  return result;
}
// Tooltip helper
function setTooltip(element, text) {
  element.title = text;
}
// Export
window.Zinkro = {
  gregorianToHolocene,
  holoceneToGregorian,
  formatHolocene,
  gregorianToZinkro,
  zinkroToGregorian,
  setTooltip
};
