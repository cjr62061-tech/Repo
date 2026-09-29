from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", "B", 16)
pdf.cell(200, 10, "Chemistry Formulas - Soil Art Edition", ln=True, align='C')
pdf.ln(10)

pdf.set_font("Arial", "", 12)
formulas = [
    "1. PV = nRT (Ideal Gas)",
    "2. pH = -log [H+]",
    "3. Moles = Mass / Molar Mass",
    "4. Molarity = Moles / Volume(L)",
    "5. Density = Mass / Volume",
    "6. E = h * v",
    "7. Rate = k [A]^m [B]^n",
    "8. Kc = [Products]/[Reactants]",
]

for f in formulas:
    pdf.cell(0, 10, f, ln=True)

pdf.output("chemistry_formulas.pdf")
print("PDF Ready!")