import './globals.css';
import { Toaster } from "@/components/ui/toaster";
import { Header } from "@/components/layout/header";

export const metadata = {
  title: 'GeoPulse',
  description: 'Simple website for GeoPulse project',
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="true" />
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&family=Cormorant+Garamond:wght@700&display=swap" rel="stylesheet" />
      </head>
      <body className="font-body antialiased min-h-screen flex flex-col">
        <Header />
        <main className="flex-1 grid">{children}</main>
        <Toaster />
      </body>
    </html>
  );
}
