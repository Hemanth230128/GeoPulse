import Link from 'next/link';
import { MountainIcon, Menu } from 'lucide-react';
import { Button } from '@/components/ui/button';
import { Sheet, SheetContent, SheetTrigger } from '@/components/ui/sheet';
import { MainNav } from './main-nav';

export function Header() {
  return (
    <header className="sticky top-0 z-40 flex h-16 items-center gap-4 border-b bg-background px-4 md:px-6">
      <Link href="/" className="flex items-center gap-2 font-semibold">
        <MountainIcon className="h-6 w-6 text-primary" />
        <span className="text-lg">Geopulse Navigator</span>
      </Link>
      <nav className="hidden flex-1 items-center justify-center md:flex">
        <MainNav />
      </nav>
      <div className="flex items-center gap-4 md:ml-auto md:hidden">
        <Sheet>
          <SheetTrigger asChild>
            <Button variant="outline" size="icon">
              <Menu className="h-5 w-5" />
              <span className="sr-only">Toggle navigation menu</span>
            </Button>
          </SheetTrigger>
          <SheetContent side="right">
            <nav className="grid gap-6 text-lg font-medium">
              <Link
                href="/"
                className="flex items-center gap-2 text-lg font-semibold"
              >
                <MountainIcon className="h-6 w-6 text-primary" />
                <span className="sr-only">Geopulse Navigator</span>
              </Link>
              <MainNav mobile />
            </nav>
          </SheetContent>
        </Sheet>
      </div>
    </header>
  );
}
