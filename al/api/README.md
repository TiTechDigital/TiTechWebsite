# TiTech Digital Contact Form API

This directory contains Vercel serverless functions for handling contact form submissions via Resend email service.

## Setup

### 1. Install Dependencies

```bash
npm install
```

### 2. Configure Environment Variable on Vercel

Add your Resend API key to Vercel environment variables:

1. Go to your Vercel project dashboard
2. Navigate to **Settings** → **Environment Variables**
3. Add new variable:
   - **Name**: `RESEND_API_KEY`
   - **Value**: Your Resend API key (starts with `re_`)
   - **Environment**: Production, Preview, Development (select all)

### 3. Verify Domain on Resend

Before sending emails, verify your domain on Resend:

1. Go to [Resend Dashboard](https://resend.com/domains)
2. Add domain: `titechdigital.it`
3. Add the provided DNS records (SPF, DKIM, DMARC)
4. Wait for verification (usually takes a few minutes)

## API Endpoint

**POST** `/api/send-email`

### Request Body

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "message": "I need a website",
  "phone": "+39 123 456 7890",      // optional
  "company": "Example Corp",         // optional
  "service": "Sito web",            // optional
  "language": "it",                 // "it" or "en"
  "attribution": {                  // optional
    "source": "google",
    "medium": "organic",
    "campaign": "summer2024"
  }
}
```

### Response

**Success (200)**:
```json
{
  "success": true,
  "messageId": "uuid-from-resend",
  "message": "Richiesta inviata con successo"
}
```

**Error (400/500)**:
```json
{
  "error": "Error message in appropriate language"
}
```

## Testing Locally

```bash
# Install Vercel CLI
npm i -g vercel

# Run local dev server
vercel dev
```

Then test at `http://localhost:3000/api/send-email`

## Email Configuration

- **From**: `TiTech Digital Website <noreply@titechdigital.it>`
- **To**: `info@titechdigital.it`
- **Reply-To**: Customer's email address

## Form Integration

Contact forms automatically use this API. The JavaScript file `assets/js/contact-form.js` handles:

- Form validation
- API communication
- Success/error states
- Attribution tracking
- A/B test conversion tracking

## Security Features

- CORS protection (same-origin only)
- Email format validation
- Required field validation
- Rate limiting (handled by Vercel)
- API key stored securely in environment variables

## Monitoring

Monitor email delivery in your [Resend Dashboard](https://resend.com/emails).
