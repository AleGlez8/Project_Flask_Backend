import { test, expect } from '@playwright/test';

test('home page', async ({ page }) => {
    await page.goto('https://chabacano.mx/');
    await expect(page).toHaveTitle(/Joyería Chabacano México – Chabacano MX/);
    await expect(page.locator('figure[class="logo__img logo__img--color image-wrapper lazy-image"]')).toBeVisible();
    await first.locator('summary[class="navlink navlink--search"]').click();
    const searchInput = page.locator('input[id="SearchInput--mobile"]');
    await expect(searchInput).toBeVisible();

});

test('navigation links', async ({ page }) => {
    // Ir a la página principal
    await page.goto('https://chabacano.mx/');

    // Verificar el enlace a la página 'Aretes'
    await page.click('a[href="/collections/aretes"]');
    await expect(page).toHaveURL('https://chabacano.mx/collections/aretes');
    // Volver a la página principal
    await page.goBack();

    // Verificar el enlace a la página 'Anillos'
    await page.click('a[href="/collections/anillos"]');
    await expect(page).toHaveURL('https://chabacano.mx/collections/anillos');
    await page.goBack();

    // Verificar el enlace a la página 'Collares'
    await page.click('a[href="/collections/collares"]');
    await expect(page).toHaveURL('https://chabacano.mx/collections/collares');
    await page.goBack();

    // Verificar el enlace a la página 'Pulseras'
    await page.click('a[href="/collections/pulseras"]');
    await expect(page).toHaveURL('https://chabacano.mx/collections/pulseras');
    await page.goBack();
});

test('add to cart', async ({ page }) => {
    await page.goto('https://chabacano.mx/');
});

test('add to cart and checkout without login', async ({ page }) => {
    await page.goto('https://chabacano.mx/');
});

test('add to cart and checkout with login', async ({ page }) => {
    await page.goto('https://chabacano.mx/');
});