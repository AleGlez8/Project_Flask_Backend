import { test, expect } from '@playwright/test';

test('navegar a la página principal', async ({ page }) => {
    await page.goto('https://chabacano.mx/');
    await expect(page).toHaveTitle(/Joyería Chabacano México – Chabacano MX/);
});

test('verificar texto de bienvenida', async ({ page }) => {
    await page.goto('https://chabacano.mx/');
    const welcomeText = await page.textContent('h1');  // Asumiendo que el texto de bienvenida está en un h1
    expect(welcomeText).toBe('¡Bienvenidos a Chabacano!');  // Ajusta el texto esperado según corresponda
});

test('verificar navegación de enlaces', async ({ page }) => {
    await page.goto('https://chabacano.mx/');
    await page.click('text=Productos');  // Supón que hay un enlace o botón de Productos
    await expect(page).toHaveURL(/.*productos/);  // Verifica que la URL cambie adecuadamente
});
