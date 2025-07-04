import {
  SidebarProvider,
  Sidebar,
  SidebarInset,
  SidebarTrigger,
} from '@/components/ui/sidebar';
import { SidebarNav } from '@/components/sidebar-nav';
import { Home, ChevronRight } from 'lucide-react';
import Link from 'next/link';

export default function SectionLayout({
  children,
  params,
}: {
  children: React.ReactNode;
  params: { sectionId: string };
}) {
  return (
    <SidebarProvider>
      <div className="flex h-full">
        <Sidebar>
          <SidebarNav sectionId={params.sectionId} />
        </Sidebar>
        <SidebarInset>
          <header className="sticky top-16 z-10 flex h-14 items-center gap-4 border-b bg-background px-4 sm:static sm:h-auto sm:border-0 sm:bg-transparent sm:px-6 md:top-0">
            <SidebarTrigger className="md:hidden" />
            <div className="flex items-center gap-2 text-sm text-muted-foreground">
              <Link href="/" className="hover:text-primary">
                <Home className="h-4 w-4" />
              </Link>
              <ChevronRight className="h-4 w-4" />
              <span>Section {params.sectionId}</span>
            </div>
          </header>
          <div className="p-4 sm:p-6">{children}</div>
        </SidebarInset>
      </div>
    </SidebarProvider>
  );
}
