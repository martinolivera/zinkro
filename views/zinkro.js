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
// Retorna: (year, month, day) donde month y day pueden ser null
// - (year, null, 0) = Día Zero
// - (year, null, 366) = Día 366 (solo bisiestos)
// - (year, month, day) = fecha normal
function gregorianToZinkro(dateStr) {
  // dateStr: "YYYY-MM-DD"
  const [year, month, day] = dateStr.split('-').map(Number);
  
  function isLeap(year) {
    return (year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0);
  }
  
  // CASO 1: 20 de marzo = Día Zero
  if (month === 3 && day === 20) {
    return { year: gregorianToHolocene(year), month: null, day: 0 };
  }
  
  // Determinar a qué año Zinkro pertenece
  let yearZ, year_ref;
  if (month < 3 || (month === 3 && day < 20)) {
    // Antes del 20 de marzo: año anterior
    yearZ = gregorianToHolocene(year - 1);
    year_ref = year - 1;
  } else {
    // Después del 20 de marzo: año actual
    yearZ = gregorianToHolocene(year);
    year_ref = year;
  }
  
  // CASO 2: Después del 20 de marzo (21/3 - 31/3 - ... - 19/3 siguiente)
  if (month === 3 && day > 20) {
    return { year: yearZ, month: 1, day: day - 20 };
  }
  
  // CASO 3: Abril a diciembre
  if (month > 3) {
    const march21 = new Date(year, 2, 21); // 21 de marzo (month es 0-indexed)
    const currentDate = new Date(year, month - 1, day);
    const daysSince = Math.floor((currentDate - march21) / (24 * 60 * 60 * 1000));
    
    const monthZ = Math.floor(daysSince / 28) + 1;
    const dayZ = daysSince % 28 + 1;
    return { year: yearZ, month: monthZ, day: dayZ };
  }
  
  // CASO 4: Antes del 20 de marzo (enero, febrero, 1-19 de marzo)
  const march20Ref = new Date(year_ref, 2, 20); // 20 de marzo del año anterior
  const currentDate = new Date(year, month - 1, day);
  const daysSinceZero = Math.floor((currentDate - march20Ref) / (24 * 60 * 60 * 1000));
  
  const isLeapCurrent = isLeap(year);
  
  if (daysSinceZero <= 364) {
    const monthZ = Math.floor((daysSinceZero - 1) / 28) + 1;
    const dayZ = (daysSinceZero - 1) % 28 + 1;
    return { year: yearZ, month: monthZ, day: dayZ };
  } else if (daysSinceZero === 365 && isLeapCurrent) {
    // Día 366 especial en año bisiesto (19 de marzo cuando el año actual es bisiesto)
    return { year: yearZ, month: null, day: 366 };
  }
  
  throw new Error(`Fecha fuera de rango: ${dateStr}`);
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
  setTooltip
};
