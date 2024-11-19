import { test, expect } from '@playwright/test';

test('navegar a la página principal', async ({ page }) => {
    await page.goto('https://chabacano.mx/');
    await expect(page).toHaveTitle(/Joyería Chabacano México – Chabacano MX/);
});

test('verificar enlaces de navegación', async ({ page }) => {
    // Ir a la página principal
    await page.goto('https://chabacano.mx/');

    // Verificar el enlace a la página 'Anillos'
    await page.click('a[href="/collections/anillos"]');
    await expect(page).toHaveURL('https://chabacano.mx/collections/anillos');

    // Volver a la página principal
    await page.goBack();

    // Verificar el enlace a la página 'Contacto'
    await page.click('a[href="/collections/pulseras"]');
    await expect(page).toHaveURL('https://chabacano.mx/collections/pulseras');
});
