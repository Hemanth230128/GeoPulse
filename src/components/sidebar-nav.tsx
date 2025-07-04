'use client';

import { usePathname } from 'next/navigation';
import Link from 'next/link';
import {
  SidebarContent,
  SidebarHeader,
  SidebarMenu,
  SidebarMenuItem,
  SidebarMenuButton,
} from '@/components/ui/sidebar';
import { cn } from '@/lib/utils';
import { Separator } from './ui/separator';

const subsections = [
  { id: 'a', name: 'Subsection A' },
  { id: 'b', name: 'Subsection B' },
  { id: 'c', name: 'Subsection C' },
];

export function SidebarNav({ sectionId }: { sectionId: string }) {
  const pathname = usePathname();

  return (
    <div className="flex flex-col h-full">
      <SidebarHeader>
        <h2 className="text-xl font-semibold text-sidebar-foreground">
          Section {sectionId}
        </h2>
        <Separator className="my-2 bg-sidebar-border" />
      </SidebarHeader>
      <SidebarContent>
        <SidebarMenu>
          {subsections.map((subsection) => (
            <SidebarMenuItem key={subsection.id}>
              <SidebarMenuButton
                asChild
                isActive={pathname === `/section/${sectionId}/${subsection.id}`}
                className={cn(
                  'justify-start',
                  pathname === `/section/${sectionId}/${subsection.id}`
                    ? 'bg-sidebar-accent text-sidebar-accent-foreground'
                    : 'hover:bg-sidebar-accent'
                )}
              >
                <Link href={`/section/${sectionId}/${subsection.id}`}>
                  {subsection.name}
                </Link>
              </SidebarMenuButton>
            </SidebarMenuItem>
          ))}
        </SidebarMenu>
      </SidebarContent>
    </div>
  );
}
